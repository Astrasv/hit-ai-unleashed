from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from tavily import TavilyClient

from dotenv import load_dotenv

load_dotenv()

# Tool for web search
@tool("web_search", return_direct=True, description="Perform a web search and return the results.")
def web_search(query: str) -> str:
    client = TavilyClient()
    results = client.search(query)
    return results

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
)


agent_without_tool = create_agent(
    model=model,
    tools=[],
)

agent_with_tool = create_agent(
    model=model,
    tools=[web_search],
)


response_without_tool = agent_without_tool.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the 2026 result of tamilnadu election"
            }
        ]
    }
)

print(response_without_tool["messages"][-1].content)

# response_with_tool = agent_with_tool.invoke(
#     {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "What is the 2026 result of tamilnadu election"
#             }
#         ]
#     }
# )

# print(response_with_tool["messages"][-1].content)