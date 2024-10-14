from enum import Enum
from typing import Annotated
from pydantic import BaseModel, BeforeValidator, Field
from bson import ObjectId

class Book(BaseModel):
    title:str
    price:float
    theme:str

class Book_ID(Book):
    id: Annotated[str,BeforeValidator(str),Field(alias="_id")]
