from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from schema import WonderResponse, ListOfResponse

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",  
)



agent = create_agent(
    model=model,
    response_format=ListOfResponse, # Show both List and No list

    # Show about an intentional mistake in schema
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Give me the 7 wonders of the world"
            }
        ]
    }
)



print(response["structured_response"])


for item in response["structured_response"].result:
    print(item.name)
    print(item.description)
    print(item.rating)
    print(item.coutnry)
    print()