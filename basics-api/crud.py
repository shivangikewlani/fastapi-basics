from models.py import User
from schemas import LoginUser
from fastapi import FastAPI, Request, Response, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from fastapi.responses import JSONResponse
from auth import hash_password, verify_password, create_access_token, decode_token

app = FastAPI()
 
db_name = 'crud.db'
connection = create_engine(f"sqlite///{db_name}", echo = True)

@app.on_event("startup")
def create_session():
    SQLModel.metadata.create_all(connection)

@app.post("/login")
async def user_login(user: LoginUser):
    with Session(connection) as session:
        exist_user = session.exec(select(User).where(User.email == user.email)).first()
        if not exist_user or not verify_password(user.password, exist_user.password):
            raise HTTPException(status_code = 400, detail = 'User not found')
        token_data = {"username" : user.email}
        access_token = create_access_token(token_data)
    return{"access_token": access_token, "token_type": "bearer"}

@app.post("/register")
async def register_user(user: User):
    exist_user = session.exec(Select(User).where(User.email == user.email)).first()
        
        

