from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from typing import TypedDict
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
    title = title_generation_model.invoke(prompt)
    return {"title": title}


title_generation_model = model.with_structured_output(TitleGeneration)

graph = StateGraph(TitleState)
graph.add_node("title_node", title_node)
graph.add_edge(START, "title_node")
graph.add_edge("title_node", END)
title_generation_agent = graph.compile()
