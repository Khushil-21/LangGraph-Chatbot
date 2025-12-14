from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, Annotated
from dotenv import load_dotenv
import sqlite3
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import os
import requests


load_dotenv()

model = ChatOllama(model="qwen3-coder:480b-cloud")

# ------------------------- Tools Definition -------------------------

search_tool = DuckDuckGoSearchRun(region="us-en")

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}
        
        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}
    except Exception as e:
        return {"error": str(e)}

@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={os.getenv('ALPHA_VANTAGE_API_KEY')}"
    r = requests.get(url)
    return r.json()

tools = [search_tool, calculator, get_stock_price]
model_with_tools = model.bind_tools(tools)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState) -> ChatState:
    response = model_with_tools.invoke(state["messages"])
    return {"messages": [response]}

tool_node = ToolNode(tools)

connection = sqlite3.connect("chat_messages.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=connection)
graph = StateGraph(ChatState)

graph.add_node("chat bot", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat bot")
graph.add_conditional_edges("chat bot",tools_condition)
graph.add_edge("tools", "chat bot")

chatbot = graph.compile(checkpointer=checkpointer)


# def get_all_thread_ids():
#     all_thread_ids = set()
#     for checkpoint in checkpointer.list(None):
#         # print(checkpoint.config["configurable"]["thread_id"])
#         all_thread_ids.add(checkpoint.config["configurable"]["thread_id"])
#     thread_obj={thread_id:"New Chat" for thread_id in all_thread_ids}
    
#     return thread_obj
