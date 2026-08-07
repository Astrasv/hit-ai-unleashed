
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from learn_hooks.custom_hooks.humanizer import llm_humanizer_hook

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
)


agent = create_agent(
    model=model,
    middleware=[llm_humanizer_hook]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "50 word essay on friendship"
            }
        ]
    }
)

print(response["messages"][-1].content)
