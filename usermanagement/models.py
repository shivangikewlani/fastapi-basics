from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import Emailstr

class User(SQLModel, Table = true):
    id : Optional[int] = Field(primary_key = True, default = None)
    name : str
    hashed_password : str
    eemail : Emailstr