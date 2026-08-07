from pydantic import BaseModel, Field

class WonderResponse(BaseModel):
    name: str = Field(...)
    rating: float = Field(ge=0.0, le=5.0)
    description: str = Field(...)
    coutnry: str = Field(...)

class ListOfResponse (BaseModel):
    result: list[WonderResponse] = Field(...)
