from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.todo import todo_schema, todo_crud

router = APIRouter(
    prefix="/api/todo",
)


@router.get("/list", response_model=list[todo_schema.Todo])
def todo_list(db: Session = Depends(get_db)):
    _todo_list = todo_crud.get_todo_list(db)
    return _todo_list

@router.get("/detail/{todo_id}", response_model=todo_schema.Todo)
def todo_detail(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_crud.get_todo(db, todo_id=todo_id)
    return todo


