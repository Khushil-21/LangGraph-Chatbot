from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage,HumanMessage,SystemMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict ,Annotated
from dotenv import load_dotenv


load_dotenv()

model = ChatOllama(model="gemma3:1b")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    
def chat_node(state:ChatState)->ChatState:
    response = model.invoke(state["messages"])
    return {"messages":[response]}


checkpointer = InMemorySaver()
graph = StateGraph(ChatState)
graph.add_node("chat bot",chat_node)
graph.add_edge(START, "chat bot")
graph.add_edge("chat bot", END)

chat_bot = graph.compile(checkpointer=checkpointer)