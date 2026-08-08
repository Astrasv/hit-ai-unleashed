from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage
from schemas.models import JokeRequest, JokeResponse
from services.agents import graph

router = APIRouter()

@router.post("/generate-joke", response_model=JokeResponse)
async def generate_joke(request: JokeRequest):
    try:
        prompt = f"Tell me a brief joke about {request.topic}"
        initial_input = {"messages": [HumanMessage(content=prompt)]}
        
        final_state = await graph.ainvoke(initial_input)
        
        return final_state["joke"]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))