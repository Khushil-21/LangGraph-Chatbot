from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from typing import TypedDict
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from dotenv import load_dotenv
from pydantic import Field, BaseModel

load_dotenv()
model = ChatOllama(model="gemma3:1b")


class TitleGeneration(BaseModel):
    title: str = Field(
        description="From the given chat history, generate a title for the chat in 4 words or less",
        max_length=25,
    )


class TitleState(TypedDict):
    prompt_with_chat_history: str
    title: str


def title_node(state: TitleState) -> TitleState:
    prompt = f"""
    You are expert at generating titles for chat conversations.
    Here is the chat history:
    {state["prompt_with_chat_history"]}
    Generate a title for the chat in 4 words or less.
    """
    title = title_generation_model.invoke(prompt).title
    return {"title": title if title else "New Chat"}


title_generation_model = model.with_structured_output(TitleGeneration)

connection = sqlite3.connect("threads.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=connection)

graph = StateGraph(TitleState)
graph.add_node("title_node", title_node)
graph.add_edge(START, "title_node")
graph.add_edge("title_node", END)
title_generation_agent = graph.compile(checkpointer=checkpointer)

def get_all_threads_ids():
    all_thread_ids = set()
    for checkpoint in checkpointer.list(None):
        id=checkpoint.config["configurable"]["thread_id"]
        all_thread_ids.add(id)
    return list(all_thread_ids)

def get_all_threads():
    all_thread_ids = get_all_threads_ids()
    all_thread_ids_obj = {}
    for thread_id in all_thread_ids:
        state=title_generation_agent.get_state(config={"configurable": {"thread_id": f"{thread_id}"}}).values
        all_thread_ids_obj[thread_id] = state["title"] if state["title"] else "New Chat"
    print(all_thread_ids_obj)
    return all_thread_ids_obj

get_all_threads()