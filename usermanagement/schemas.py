from pydantic import BaseModel
from typing import Field

class Usercreate(BaseModel):
    name : str
    email : str
    password : str = Field(min_length=6, max_length=20)

    @validator("password")
    def validate_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must include at least one number.")
        if not any(char.isalpha() for char in v):
            raise ValueError("Password must include at least one alphabet.")
        if not any(char.isupper() for char in v):
            raise ValueError("Password must include at least one capital alphabet.")
        if not any(char in '@#$!%^&*' for cahr in v):
            raise ValueError("Password must include atleast one special character.")
        return v
        
class UserLogin(BaseModel):
    email : Emailstr
    password : str

class ShowUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token : str
    token_type : str