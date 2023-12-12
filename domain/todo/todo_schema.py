import datetime

from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    subject: str
    due_date: int
    done: str | None = None
    create_date: datetime.datetime

    class Config:
        orm_mode = True
