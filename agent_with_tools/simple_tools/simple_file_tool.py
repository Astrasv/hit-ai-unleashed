import os
import re

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Tool to get current directory
@tool("get_current_directory", description="Get the current working directory.")
def get_current_directory() -> str:
    return os.getcwd()

@tool("search_files", description="Search for files in a directory using a regex pattern.")
def search_files(directory: str, pattern: str) -> list[str]:
    """
    Search for files in a directory using a regex pattern.
    """
    files = os.listdir(directory)
    regex = re.compile(pattern)

    return [f for f in files if regex.search(f)]


@tool("read_files", description="Read the files in a directory.")
def read_files(directory: str) -> list[str]:
    """
    List all files in a directory.
    """
    return os.listdir(directory)


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
)

agent = create_agent(
    model=model,
    tools=[search_files, read_files, get_current_directory],
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "List files in the current directory that are NOT related to Python"
            }
        ]
    }
)

print(response["messages"][-1].content)