import streamlit as st

if "messages" not in st.session_state:
    st.session_state["messages"] = []


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Enter a message:")

if user_input:
    # store the user input in the session state
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # store the assistant response in the session state
    st.session_state["messages"].append({"role": "assistant", "content": user_input})
    with st.chat_message("assistant"):
        st.text(user_input)
