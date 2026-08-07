from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()

class AgentState(TypedDict):
    messages: list[BaseMessage]

def call_model(state: AgentState):
    model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
    response = model.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

builder = StateGraph(AgentState)
builder.add_node("joke_agent", call_model)

builder.add_edge(START, "joke_agent")
builder.add_edge("joke_agent", END)

graph = builder.compile()

initial_input = {"messages": [HumanMessage(content="Tell me a brief joke about databases")]}
final_state = graph.invoke(initial_input)

print(final_state["messages"][-1].content)