from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openrouter import ChatOpenRouter

from dotenv import load_dotenv

load_dotenv()

checkpointer = InMemorySaver()

model = ChatOpenRouter(
    model="google/gemma-4-31b-it:free",
)

summarization_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        SummarizationMiddleware(
            model=summarization_model,
            trigger=("messages", 3),
            keep=("messages", 2),
        )
    ],
    checkpointer=checkpointer,
)

config: RunnableConfig = {
    "configurable": {"thread_id": "1"}
}

agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "hi, my name is bob"}
        ]
    },
    config,
)

agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "write a short poem about cats"}
        ]
    },
    config,
)

agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "now do the same but for dogs"}
        ]
    },
    config,
)

final_response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "what's my name?"}
        ]
    },
    config,
)

final_response["messages"][-1].pretty_print()

state = agent.get_state(config)

print(state.values.keys())
print(state.values.get("summary"))