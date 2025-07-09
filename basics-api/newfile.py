from fastapi import FastAPI, Request, Response
import dicttoxml
from pydantic import BaseModel, EmailStr, Field, constr
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel

app = FastAPI()

@app.get('/details')
async def detail(request:Request):
    data = {
        "name" : "Shivangi",
        "age" : 33
    }
    header_val = request.headers.get("accept")
    print(header_val)
    if 'application/xml' in header_val:
        xmldata = dicttoxml.dicttoxml(data, custom_root = 'deatil', attr_type = False)
        return Response(content = xmldata, media_type="application/xml")
    else:
        return JSONResponse(content = data)

class User(BaseModel):
    name : str
    email : EmailStr

@app.post('/register-detail/{user_id}')
async def register(user_id:int, user:User):
    return {"name" : user.name}

