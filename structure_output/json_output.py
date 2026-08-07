from dotenv import load_dotenv


from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()



model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
)

agent = create_agent(model=model)


response =  agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Give me a JSON as output which has the country,place,name of the 7 wonders of the world"
            }
        ]
    }
)

print(response["messages"][-1].content)

