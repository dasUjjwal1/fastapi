import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:6700"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
app = FastAPI()


class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoBase(BaseModel):
    id: int


class TblTodo(Base):
    __tablename__ = "todos"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    title = Column(String)
    completed = Column(Boolean, insert_default=False)


@app.post("/todos", response_model=TodoBase)
async def create_todo(payload: TodoCreate) -> TodoBase:
    """_summary_

    Args:
        payload (Todo): _description_

    Returns:
        TodoId: _description_
    """


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
