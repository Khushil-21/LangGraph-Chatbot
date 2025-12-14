import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from backend_with_tool import chatbot
from tittle_with_tool import get_all_threads
from tittle_with_tool import title_generation_agent
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
                role = "user"
            else:
                role = "assistant"
            all_messages.append({"role": role, "content": message.content})
        st.session_state["message_history"] = all_messages
    else:
        st.session_state["message_history"] = []


def switch_thread(thread_id):
    st.session_state["current_thread_id"] = thread_id
    load_message_history(thread_id)


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

# if "message_history" not in st.session_state:
#     st.session_state["message_history"] = []


# CONFIG = {"configurable": {"thread_id": st.session_state["current_thread_id"]}}
CONFIG = {
    "configurable": {"thread_id": st.session_state["current_thread_id"]},
    "metadata": {"thread_id": st.session_state["current_thread_id"]},
    "run_name":"chatbot"
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
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Enter a message:")

if user_input:
    # store the user input in the session state
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):
        # Use a mutable holder so the generator can set/modify it
        status_holder = {"box": None}

        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            ):
                # Lazily create & update the SAME status container when any tool runs
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
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

                # Stream ONLY assistant tokens
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

        # Finalize only if a tool was actually used
        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tool finished", state="complete", expanded=False
            )

        # Save assistant message
        st.session_state["message_history"].append(
            {"role": "assistant", "content": ai_message}
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
            config={**CONFIG,"run_name":"title generation"},
        )
        save_thread_title(title_response["title"])
        st.rerun()
