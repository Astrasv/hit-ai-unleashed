from pydantic import BaseModel, Field

class WonderResponse(BaseModel):
    name: str = Field(...)
    rating: float = Field(le=0.0, ge=5.0)
    #  Show different field params
    
    description: str = Field(...)
    coutnry: str = Field(...)

class ListOfResponse (BaseModel):
    result: list[WonderResponse] = Field(...)
