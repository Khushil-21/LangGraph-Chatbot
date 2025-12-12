import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot
from utils import get_thread_id

# ------------------------- Helper Functions -------------------------


def load_message_history(thread_id):
    loaded_messages = chatbot.get_state(
        config={"configurable": {"thread_id": thread_id}}
    ).values.get("messages", [])
    # Check if messages key exists in state values, return empty list if not
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
    st.session_state["all_threads"].append(new_thread_id)
    st.session_state["message_history"] = []
    switch_thread(new_thread_id)


# ------------------------- Loading Session State  -------------------------

if "all_threads" not in st.session_state:
    st.session_state["all_threads"] = []

if "current_thread_id" not in st.session_state:
    thread_id = get_thread_id()
    st.session_state["current_thread_id"] = thread_id
    st.session_state["all_threads"].append(thread_id)

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


CONFIG = {"configurable": {"thread_id": st.session_state["current_thread_id"]}}

st.title(f"Chatbot - {st.session_state['current_thread_id']}")

st.sidebar.title(f"LangGraph Chatbot")
st.sidebar.button("New Chat", on_click=new_chat)
st.sidebar.header("Past Chats")
for thread_id in st.session_state["all_threads"][::-1]:
    st.sidebar.button(
        f"Thread ID: {thread_id}", on_click=switch_thread, args=(thread_id,)
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
