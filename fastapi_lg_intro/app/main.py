from fastapi import FastAPI
from dotenv import load_dotenv
from api.routes import router

load_dotenv()

app = FastAPI(
    title="Langgraph sample API",
    description="Generate jokes y'all",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

@app.get("/")
async def health_check():
    return {"status": "healthy", "message": "API is running."}