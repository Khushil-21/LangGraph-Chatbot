from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, Annotated
from dotenv import load_dotenv
import sqlite3


load_dotenv()

model = ChatOllama(model="gemma3:1b")


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState) -> ChatState:
    response = model.invoke(state["messages"])
    return {"messages": [response]}


connection = sqlite3.connect("chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=connection)
graph = StateGraph(ChatState)
graph.add_node("chat bot", chat_node)
graph.add_edge(START, "chat bot")
graph.add_edge("chat bot", END)

chatbot = graph.compile(checkpointer=checkpointer)


def get_all_thread_ids():
    all_thread_ids = set()
    for checkpoint in checkpointer.list(None):
        # print(checkpoint.config["configurable"]["thread_id"])
        all_thread_ids.add(checkpoint.config["configurable"]["thread_id"])
    thread_obj={thread_id:"New Chat" for thread_id in all_thread_ids}
    
    return thread_obj
