from pydantic import BaseModel, Field

class JokeRequest(BaseModel):
    topic: str = Field(default="databases", description="The topic of the joke")

class JokeResponse(BaseModel):
    joke: str