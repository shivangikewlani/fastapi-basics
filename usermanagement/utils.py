from passlib.context import CryptContext
pwd_hash = CryptContext(schemas = ["bcrypt"], deprecated = "auto")

def hash_password(password:str):
    return pwd_hash.hash(password)
    
def verify_password(password:str, hashed_pwd:str)->bool:
    return pwd_hash.verify(password, hashed_pwd)