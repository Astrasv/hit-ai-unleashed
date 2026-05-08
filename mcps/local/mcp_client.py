import asyncio
import os
import sys
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
# Use the stable path for the prebuilt agent


from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import HumanMessage

load_dotenv()

async def main():
    server_script = os.path.abspath("D:/A_Projects/A_ Git hosted/ai_unleashed_hit/mcps/local/mcp_server.py")

    client = MultiServerMCPClient(
        {
            "local_server": {
                "command": sys.executable,
                "args": [server_script],
                "transport": "stdio",
            }
        }
    )


    async with client.session("local_server") as session:

        tools = await client.get_tools()
        
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        
        agent = create_agent(
            model = model, 
            tools = []
        )
        
        response = await agent.ainvoke(
            {"messages": [HumanMessage(content="Tell me about the langchain-mcp-adapters library")]}
        )
        print("\nFinal Response:")
        print(response["messages"][-1].content)



if __name__ == "__main__":

    # Standard boilerplate for Windows loop issues
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(main())