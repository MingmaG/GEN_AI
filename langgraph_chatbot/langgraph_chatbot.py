from langgraph.graph import StateGraph, START, END
from langchain.messages import HumanMessage
from typing import TypedDict, Annotated, List 
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver



llm = ChatOllama(model= 'gemma3:1b')

class ChatState(TypedDict):
  messages :Annotated[list[BaseMessage], add_messages]

  llm = ChatOllama(model= 'gemma3:1b' )
def chat_bot(state: ChatState):

    # take user query from state
    messages = state['messages']

    # send to llm
    response = llm.invoke(messages)

    # response store state
    return {'messages': [response]}

graph = StateGraph(ChatState)
graph.add_node('chat_bot', chat_bot)
graph.add_edge(START, 'chat_bot')
graph.add_edge('chat_bot', END)

chatbot = graph.compile(checkpointer=InMemorySaver()) 

