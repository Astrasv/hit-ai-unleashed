from langchain.agents import create_agent, AgentState

from langchain.agents.middleware import after_model
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.runtime import Runtime
from langchain.messages import HumanMessage

from typing import Any

from dotenv import load_dotenv

load_dotenv()


@after_model
def log_response(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    print(f"Here is what the model has returned: {state['messages'][-1].content}")
    return None


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

agent = create_agent(
    model=model,
    tools=[],
    middleware=[log_response],
)


response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the capital of tamilnadu?"}]}
)
