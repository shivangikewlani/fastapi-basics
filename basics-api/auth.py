from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = 'HS256'
ACCESS_SECRET_KEY = "taskify"
REFRESH_SECRET_KEY = "refresh"


pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def hash_password(password : str):
    pwd_context.hash_password(password)

def verify_password(plain : str, hashed:str):
    pwd_context.verify_password(plain, hashed)

def create_accesss_token(data:dict, expirytime:timedelta=None):
    data_to_encode = data.copy()
    expiry_time = datetime.utcnow() + (expirytime or timedelta(minutes=60))
    data_to_encode.update({"exp":expiry_time})
    return jwt.encode(data_to_encode, ACCESS_SECRET_KEY, algorithm=ALGORITHM)

def refresh_access_token(data: dict, expiry_time:timedelta=None):
    data_encode = data.copy()
    expirytime = datetime.utcnow() + timedelta(days=7)
    data_encode.update({"exp":expirytime})
    return jwt.encode(data_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token:str):
    try:
        payload = jwt.decode(token, ACCESS_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print {str(e)}
        return None


