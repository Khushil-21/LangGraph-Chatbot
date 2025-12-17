import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from backend import chatbot, ingest_pdf, thread_document_metadata
from tittle_generation import get_all_threads
from tittle_generation import title_generation_agent
import uuid

# ------------------------- Helper Functions -------------------------


def get_thread_id():
    thread_id = str(uuid.uuid4())
    return thread_id


def load_message_history(thread_id):
    state = chatbot.get_state(config={"configurable": {"thread_id": thread_id}}).values
    loaded_messages = state.get("messages", [])

    if loaded_messages:
        all_messages = []
        for message in loaded_messages:
            if isinstance(message, HumanMessage):
                all_messages.append({"role": "user", "content": message.content})
            elif isinstance(message, AIMessage):
                # Check if this AI message has tool calls
                tool_calls = getattr(message, "tool_calls", [])
                if tool_calls:
                    # Store tool calls info for UI rendering
                    all_messages.append(
                        {
                            "role": "assistant",
                            "content": message.content,
                            "tool_calls": tool_calls,
                        }
                    )
                else:
                    all_messages.append(
                        {"role": "assistant", "content": message.content}
                    )
            elif isinstance(message, ToolMessage):
                # Store tool messages separately for proper UI rendering
                tool_name = getattr(message, "name", "tool")
                all_messages.append(
                    {"role": "tool", "tool_name": tool_name, "content": message.content}
                )
        st.session_state["message_history"] = all_messages
    else:
        st.session_state["message_history"] = []


def switch_thread(thread_id):
    st.session_state["current_thread_id"] = thread_id
    load_message_history(thread_id)
    st.session_state["ingested_documents"].setdefault(str(thread_id), {})


def new_chat():
    new_thread_id = get_thread_id()
    st.session_state["all_threads"][new_thread_id] = "New Chat"
    st.session_state["message_history"] = []
    switch_thread(new_thread_id)


def save_thread_title(title):
    print("Saving thread title", title)
    st.session_state["all_threads"][st.session_state["current_thread_id"]] = title


# ------------------------- Loading Session State  -------------------------

if "all_threads" not in st.session_state:
    st.session_state["all_threads"] = get_all_threads()

if "current_thread_id" not in st.session_state:
    # thread_id = get_thread_id()
    thread_id = list(st.session_state["all_threads"].keys())[-1]
    st.session_state["current_thread_id"] = thread_id
    # st.session_state["all_threads"][thread_id] = "New Chat"
    load_message_history(thread_id)

if "ingested_documents" not in st.session_state:
    st.session_state["ingested_documents"] = {}

# if "message_history" not in st.session_state:
#     st.session_state["message_history"] = []

thread_docs = st.session_state["ingested_documents"].setdefault(
    str(st.session_state["current_thread_id"]), {}
)

# CONFIG = {"configurable": {"thread_id": st.session_state["current_thread_id"]}}
CONFIG = {
    "configurable": {"thread_id": st.session_state["current_thread_id"]},
    "metadata": {"thread_id": st.session_state["current_thread_id"]},
    "run_name": "chatbot",
}


# ------------------------- Tools Node Definition -------------------------

st.title(f"{st.session_state['all_threads'][st.session_state['current_thread_id']]}")
st.caption(f"Thread ID: {st.session_state['current_thread_id']}")


st.sidebar.title(f"LangGraph Chatbot")
st.sidebar.button(
    "Start New Chat",
    on_click=new_chat,
    type="primary",
    width="stretch",
    icon=":material/add:",
)

if thread_docs:
    latest_doc = list(thread_docs.values())[-1]
    st.sidebar.success(
        f"Using `{latest_doc.get('filename')}` "
        f"({latest_doc.get('chunks')} chunks from {latest_doc.get('documents')} pages)"
    )
else:
    st.sidebar.info("No PDF indexed yet.")

uploaded_pdf = st.sidebar.file_uploader("Upload a PDF for this chat", type=["pdf"])
if uploaded_pdf:
    if uploaded_pdf.name in thread_docs:
        st.sidebar.info(f"`{uploaded_pdf.name}` already processed for this chat.")
    else:
        with st.sidebar.status("Indexing PDF…", expanded=True) as status_box:
            summary = ingest_pdf(
                uploaded_pdf.getvalue(),
                thread_id=str(st.session_state["current_thread_id"]),
                filename=uploaded_pdf.name,
            )
            thread_docs[uploaded_pdf.name] = summary
            status_box.update(label="✅ PDF indexed", state="complete", expanded=False)


st.sidebar.divider()
st.sidebar.header("Past Chats")
# st.sidebar.write(st.session_state["all_threads"])
for thread_id, title in reversed(list(st.session_state["all_threads"].items())):
    st.sidebar.button(
        key=thread_id,
        label=f"{title}",
        on_click=switch_thread,
        args=(thread_id,),
        width="stretch",
        type=(
            "secondary"
            if thread_id != st.session_state["current_thread_id"]
            else "primary"
        ),
        # disabled=thread_id == st.session_state["current_thread_id"],
        icon=":material/chat:",
    )


for message in st.session_state["message_history"]:
    if message["role"] == "tool":
        # Skip tool messages in main display - they'll be shown in assistant's status box
        continue

    with st.chat_message(message["role"]):
        # Check if this is an assistant message with tool calls
        if message["role"] == "assistant" and message.get("tool_calls"):
            # Find associated tool messages
            msg_index = st.session_state["message_history"].index(message)
            tool_messages = []

            # Collect all tool messages that follow this AI message
            for i in range(msg_index + 1, len(st.session_state["message_history"])):
                next_msg = st.session_state["message_history"][i]
                if next_msg["role"] == "tool":
                    tool_messages.append(next_msg)
                else:
                    break

            # Display tool usage in a status box
            if tool_messages:
                with st.status("🔧 Used tools", expanded=False):
                    for tool_msg in tool_messages:
                        st.markdown(f"**{tool_msg['tool_name']}**")
                        st.code(tool_msg["content"], language="json")

        # Display the assistant's content
        if message["content"]:
            st.markdown(message["content"])

user_input = st.chat_input("Enter a message:")

if user_input:
    # store the user input in the session state
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):
        # Use a mutable holder so the generator can set/modify it
        status_holder = {"box": None, "tool_messages": []}
        tool_calls_info = []

        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            ):
                # Handle tool messages
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    tool_content = message_chunk.content

                    # Store tool message info
                    status_holder["tool_messages"].append(
                        {"tool_name": tool_name, "content": tool_content}
                    )

                    # Create or update status box
                    if status_holder["box"] is None:
                        status_holder["box"] = st.status(
                            f"🔧 Using `{tool_name}` …", expanded=True
                        )
                    else:
                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` …",
                            state="running",
                            expanded=True,
                        )

                    # Display tool content inside status box
                    with status_holder["box"]:
                        st.markdown(f"**{tool_name}**")
                        st.code(tool_content, language="json")

                # Capture tool calls from AI messages
                if isinstance(message_chunk, AIMessage):
                    if (
                        hasattr(message_chunk, "tool_calls")
                        and message_chunk.tool_calls
                    ):
                        tool_calls_info.extend(message_chunk.tool_calls)
                    # Stream ONLY assistant tokens
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

        # Finalize only if a tool was actually used
        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tools used", state="complete", expanded=False
            )

        # Save assistant message with tool calls info if any
        if tool_calls_info:
            st.session_state["message_history"].append(
                {
                    "role": "assistant",
                    "content": ai_message,
                    "tool_calls": tool_calls_info,
                }
            )
        else:
            st.session_state["message_history"].append(
                {"role": "assistant", "content": ai_message}
            )

        # Save tool messages to history
        for tool_msg in status_holder["tool_messages"]:
            st.session_state["message_history"].append(
                {
                    "role": "tool",
                    "tool_name": tool_msg["tool_name"],
                    "content": tool_msg["content"],
                }
            )

    doc_meta = thread_document_metadata(str(st.session_state["current_thread_id"]))
    if doc_meta:
        st.caption(
            f"Document indexed: {doc_meta.get('filename')} "
            f"(chunks: {doc_meta.get('chunks')}, pages: {doc_meta.get('documents')})"
        )
    
    if (
        st.session_state["all_threads"][st.session_state["current_thread_id"]]
        == "New Chat"
        and len(st.session_state["message_history"]) >= 3
    ):
        title_response = title_generation_agent.invoke(
            {
                "prompt_with_chat_history": f"Here is the chat history: {st.session_state["message_history"]}"
            },
            config={**CONFIG, "run_name": "title generation"},
        )
        save_thread_title(title_response["title"])
        st.rerun()

st.divider()
