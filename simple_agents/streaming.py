from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from dotenv import load_dotenv

from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()



model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
)

agent = create_agent(model=model)

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(user_input: str):
    async def event_generator():
        async for token, metadata in agent.astream(
            {"messages": [HumanMessage(content=user_input)]},
            stream_mode="messages",
        ):
            if token.content:
                yield token.content 

    return StreamingResponse(event_generator(), media_type="text/event-stream")