from fastapi import FastAPI
from pydantic import BaseModel,Field

class AuthorCreate(BaseModel):
    name: str = Field(max_length=2,max_digits=100)
    country: str = Field(max_length=2,max_digits=60)
    birth_year: int | None
    
class 