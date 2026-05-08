from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.messages import HumanMessage

import base64

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)


agent= create_agent(
    model=model,
    tools=[],
)


file_path = "./multimodal/image.png"    
with open(file_path, "rb") as image_file:
        # read() returns bytes, which base64 expects
        img_bytes = image_file.read()


img_b64 = base64.b64encode(img_bytes).decode('utf-8')

multimodal_question = HumanMessage(content=[
    {"type": "text", "text": "Where can I palce what furnitiure in this hall"},
    {"type": "image", "base64": img_b64, "mime_type": "image/png"}
])

response = agent.invoke(
    {"messages": [multimodal_question]}
)

print(response['messages'][-1].content)
