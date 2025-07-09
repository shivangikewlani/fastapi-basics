from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, EmailStr, Field, constr
from fastapi.responses import JSONResponse, Response
import dicttoxml
from typing import Dict

# Fake in-memory database
db: Dict[str, dict] = {}

app = FastAPI()

@app.get('/userdetails')
async def get_users(request : Request):

    data ={"name":"Shanaya",
    "age":33}
    header = request.headers.get("accept")
    if 'application/xml' in header:
        xmldata = dicttoxml.dicttoxml(data, custom_root="i", attr_type=False)
        return Response(content = xmldata, media_type="application/xml")
    else:
        return JSONResponse(content = data)


class User(BaseModel):
    name:str
    age :int = Field(..., gt = 0, lt =100),
    email: EmailStr

@app.post('/Register')
async def create_user(user : User):
    if user.name in db:
        raise HTTPException(status_code = 400, message ='User already registerd')
    db[user.name] = user.dict()
    return {"message" : f"User {user.name} registered"}

class UpdateUser(BaseModel):
    age : int

@app.put("/update/{username}")
async def update_user(username: str, updates: UpdateUser):
    if username not in db:
        raise HTTPException(status_code = 404, detail="User not Found")
    db[username].update(update.dict())
    return {"message" : f"User {username} details updated",
            "data" : db[username]
            }

@app.delete('/delete/{username}')
async def delete_user(username:str):
    if username not in db:
        raise HTTPException(status_code = 404, message = "User Not Found")
    del db[username]
    return {"message" : f"Successfully {username} deleted"}