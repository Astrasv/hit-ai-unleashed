
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from learn_hooks.tools.shipping import calculate_shipping_cost

from learn_hooks.custom_hooks.log_inspect_tools import pre_tool_hook, post_tool_hook

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
)


agent = create_agent(
    model=model,
    tools=[calculate_shipping_cost],
    middleware=[pre_tool_hook, post_tool_hook]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Calculate shipping cost for a 40kg package to France"
            }
        ]
    }
)
print(response)