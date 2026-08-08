from typing import Annotated, NotRequired, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, BaseMessage

from schemas.models import JokeResponse

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    joke: NotRequired[JokeResponse]

def call_model(state: AgentState):
    model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
    structured_model = model.with_structured_output(JokeResponse)
    joke = structured_model.invoke(state["messages"])
    return {
        "joke": joke, 
        "messages": [AIMessage(content=joke.joke)]
    }


builder = StateGraph(AgentState)
builder.add_node("joke_agent", call_model)

builder.add_edge(START, "joke_agent")
builder.add_edge("joke_agent", END)

graph = builder.compile()