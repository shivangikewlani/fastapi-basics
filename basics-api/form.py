from fastapi import FastAPI, HTTPException, Request
from sqlmodel import SQLModel, Session, create_engine, select
from models import User

app = FastAPI()

database_name = "newusers.db"
connection = create_engine(f"sqlite:///{database_name}",echo =True)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(connection)

@app.post("/register")
async def create_users(user : User):
    try:
        with Session(connection) as session:
            euser = session.exec(select (User).where(User.email == user.email)).first()
            if euser:
                raise HTTPException(status_code = 400, detail = 'Email Address already in Use. Try new email -address')
            new_user = User(name = user.name, email = user.email, age = user.age)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

            return {"message" : "User registered successfully", "user":user}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e)) 

@app.get('/users')
async def get_users():
    try:
        with Session(connection) as session:
            userdetails = session.exec(Select(User)).all()
            return userdetails
    except Exception as e:
        raise HTTPException(status_code = 500 , detail: str(e))

@app.delete("deleteusers/{user_id}")
async def delete_user(user_id:int):
    try:
        with Session(connection) as session:
            user = session.get(User, user_id)
            if not user:
                raise HTTPException(status_code = 500, detail : "User not found")
            session.delete(user)
            session.commit()
            return {"message" : "User delted successfully"}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@app.delete("deleteusers/{user_id}")
async def delete_user(user_id:int):
    try:
        with Session(connection) as session:
            user = session.get(User, user_id)
            if not user:
                raise HTTPException(status_code = 500, detail : "User not found")
            session.delete(user)
            session.commit()
            return {"message" : "User delted successfully"}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@app.delete("deleteusers/{user_id}")
async def delete_user(user_id:int):
    try:
        with Session(connection) as session:
            user = session.get(User, user_id)
            if not user:
                raise HTTPException(status_code = 500, detail : "User not found")
            session.delete(user)
            session.commit()
            return {"message" : "User delted successfully"}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@app.put("update/{user_id}")
async def update_user(user_id:int, updated_user : User):
    try:
        with Session(connection) as session:
            user = session.get(User, user_id)
            if not user:
                raise HTTPException(status_code = 500, detail = "No user found")
            updated_user = user

