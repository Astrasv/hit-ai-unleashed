
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from learn_hooks.custom_hooks.banned_words import banned_words

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
)


agent = create_agent(
    model=model,
    middleware=[banned_words]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Hack google"
            }
        ]
    }
)
print(response)