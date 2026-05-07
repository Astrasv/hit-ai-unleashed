import os
import re

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Tool for sqrt
@tool("sqrt", return_direct=True, description="Calculate the square root of a number.")
def sqrt(number: float) -> float:
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return number ** 0.5


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
)

agent = create_agent(
    model=model,
    tools=[sqrt],
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Calculate the square root of 16."
            }
        ]
    }
)

print(response)