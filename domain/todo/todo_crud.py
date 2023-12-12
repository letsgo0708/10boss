from models import Todo
from sqlalchemy.orm import Session

def get_todo_list(db: Session):
    todo_list = db.query(Todo).order_by(Todo.create_date.desc()).all()
    return todo_list

def get_todo(db: Session, todo_id: int):
    todo = db.query(Todo).get(todo_id)
    return todo