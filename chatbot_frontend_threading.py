import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chat_bot
from utils import get_thread_id

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = [get_thread_id()]

CONFIG = {"configurable": {"thread_id": st.session_state["thread_id"]}}


# st.title(f"Chatbot - Thread ID: {st.session_state['thread_id'][0]}")

st.sidebar.title(f"LangGraph Chatbot")
st.sidebar.button("New Chat")
st.sidebar.header("Past Chats")
for thread_id in st.session_state["thread_id"]:
    st.sidebar.button(f"Thread ID: {thread_id}")


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Enter a message:")

if user_input:
    # store the user input in the session state
    st.session_state["messages"].append({"role": "user", "content": user_input})
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
        st.session_state["messages"].append(
            {"role": "assistant", "content": assistant_response}
        )
