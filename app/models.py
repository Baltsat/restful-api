from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int
    title: str
    year: int
    director: str
    length: str
    rating: int

class MovieCreate(BaseModel):
    title: str = Field(..., max_length=100)
    year: int = Field(..., ge=1900, le=2100)
    director: str = Field(..., max_length=100)
    length: str
    rating: int = Field(..., ge=0, le=10)