from typing_extensions import TypedDict
from typing import Literal

from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    graph_state: str


def node_1(state):
    print("---Node 1   Decision Node---")
    return {"graph_state": state['graph_state'] +" I am"}

def node_2(state):
    print("---Node 2   Happy Node---")
    return {"graph_state": state['graph_state'] +" happy!"}

def node_3(state):
    print("---Node 3   Sad Node---")
    return {"graph_state": state['graph_state'] +" sad!"}


def decide_mood(state) -> Literal["node_2", "node_3"]:
    
    user_input = state['graph_state'] 
    
    if "smile" in user_input: 
        return "node_2"

    return "node_3"


builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

graph = builder.compile()
graph.invoke({"graph_state" : "Hi smile"})

