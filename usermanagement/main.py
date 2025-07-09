from fastapi import FastAPI, Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, select
from fastapi.responses import JSONResponse
from schemas import Usercreate, Token
from utils import hash_password

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl = "login")

@app.post("/register")
async def register_user(user : Usercreate, db : Session = Depends(get_session)):
    existing_user = db.exec(select(User).where(User.email==user.email)).first()
    if existing_user:
        raise HTTPException(status_code = 400, message = 'User already present.')
    
    pwd = hash_password(user.password)
    new_user = Usercreate(name = user.name, email = user.email, password = user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message" : f"{user.name} is registered."}

@app.post("/login", response_model = Token)
async def login_user(user : )
    
'''
@app.get('/greet')
async def greet_msg(name : str, lang : str):
    if lang.lower() == 'hi':
        return {"message":f"Namaste {name} "}
    return {"message":f"Hello {name}"}

@app.get('/sum')
async def totalsum(a:int, b:int):
    return {"message":a+b}
    '''