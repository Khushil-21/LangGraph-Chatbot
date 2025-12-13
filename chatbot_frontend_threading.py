import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot
from title_generation_workflow import title_generation_agent
from utils import get_thread_id

# ------------------------- Helper Functions -------------------------


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
    st.session_state["all_threads"] = {}

if "current_thread_id" not in st.session_state:
    thread_id = get_thread_id()
    st.session_state["current_thread_id"] = thread_id
    st.session_state["all_threads"][thread_id] = "New Chat"

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


CONFIG = {"configurable": {"thread_id": st.session_state["current_thread_id"]}}

st.title(f"Chatbot - {st.session_state['current_thread_id']}")

st.sidebar.title(f"LangGraph Chatbot")
st.sidebar.button("Start New Chat", on_click=new_chat)
st.sidebar.divider()
st.sidebar.header("Past Chats")
# st.sidebar.write(st.session_state["all_threads"])
for thread_id, title in reversed(list(st.session_state["all_threads"].items())):
    st.sidebar.button(
        key=thread_id,
        label=f"{title}",
        on_click=switch_thread,
        args=(thread_id,),
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

    if (
        st.session_state["all_threads"][st.session_state["current_thread_id"]]
        == "New Chat"
        and len(st.session_state["message_history"]) >= 3
    ):
        title_response = title_generation_agent.invoke(
            {
                "prompt_with_chat_history": f"Here is the chat history: {st.session_state["message_history"]}"
            }
        )
        save_thread_title(title_response["title"].title)

    with st.chat_message("assistant"):
        assistant_response = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            )
        )
        st.session_state["message_history"].append(
            {"role": "assistant", "content": assistant_response}
        )
