import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chat_bot
from utils import get_thread_id

if "chat_history" not in st.session_state:
    thread_id = get_thread_id()
    current_thread_id = thread_id
    st.session_state["chat_history"] = {thread_id: {"messages": []}}
    st.session_state["current_thread_id"] = thread_id


def new_chat():
    new_thread_id = get_thread_id()
    st.session_state["current_thread_id"] = new_thread_id
    st.session_state["chat_history"][new_thread_id] = {"messages": []}


def switch_thread(thread_id):
    st.session_state["current_thread_id"] = thread_id


CONFIG = {"configurable": {"thread_id": st.session_state["current_thread_id"]}}

st.title(f"Chatbot - Thread ID: {st.session_state['current_thread_id']}")

st.sidebar.title(f"LangGraph Chatbot")
st.sidebar.button("New Chat", on_click=new_chat)
st.sidebar.header("Past Chats")
for thread_id in st.session_state["chat_history"]:
    st.sidebar.button(
        f"Thread ID: {thread_id}", on_click=switch_thread, args=(thread_id,)
    )


for message in st.session_state["chat_history"][st.session_state["current_thread_id"]][
    "messages"
]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Enter a message:")

if user_input:
    # store the user input in the session state
    st.session_state["chat_history"][st.session_state["current_thread_id"]][
        "messages"
    ].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):
        assistant_response = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chat_bot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            )
        )
        st.session_state["chat_history"][st.session_state["current_thread_id"]][
            "messages"
        ].append({"role": "assistant", "content": assistant_response})
