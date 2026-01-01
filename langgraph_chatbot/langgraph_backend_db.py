from langgraph.graph import StateGraph, START, END
from langchain.messages import HumanMessage
from typing import TypedDict, Annotated, List 
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3


llm = ChatOllama(model='gemma3:1b')

class ChatState(TypedDict):
  messages :Annotated[list[BaseMessage], add_messages]
  title: str

def chat_bot(state: ChatState):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response], "title": state.get("title")}



conn = sqlite3.connect(database='chatbot.DB', check_same_thread=False)

graph = StateGraph(ChatState)
graph.add_node('chat_bot', chat_bot)
graph.add_edge(START, 'chat_bot')
graph.add_edge('chat_bot', END)

checkpointer=SqliteSaver(conn=conn)
chatbot = graph.compile(checkpointer=checkpointer) 




def retrieve_all_threads():
    all_threads = {}

    for checkp in checkpointer.list(None):

        thread_id = checkp.config["configurable"]["thread_id"]
        title = checkp.metadata.get("title", "New Chat")
        all_threads[thread_id] = title

    return all_threads

