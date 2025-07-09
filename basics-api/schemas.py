from sqlmodel import BaseModel
from typing import Optional, EmailStr

class LoginUser(BaseModel):
    email : EmailStr
    pwd : str