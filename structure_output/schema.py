from pydantic import BaseModel, Field

class WonderResponse(BaseModel):
    name: str = Field(...)
    rating: float = Field(le=0.0, ge=5.0)
    description: str = Field(...)
    coutnry: str = Field(...)
    
