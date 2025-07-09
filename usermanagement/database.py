from sqlmodel import SQLModel, create_engine
sqlite_file = "sqlite:///./users.db"
engine = create_engine(sqlite_file, echo=True)

def create_database():
    SQLModel.metadata.create_all(engine)