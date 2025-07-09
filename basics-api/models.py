from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import Optional

class User(SQLModel, Table=True):
    id : Optional[int] = Field(default = None, primary_key = True)
    name : str
    email : EmailStr = Field(unique = True)
    age : int
