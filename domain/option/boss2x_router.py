from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Boss2x

from database import get_db
from domain.option import boss2x_schema

router = APIRouter(
    prefix="/api/option",
)


@router.get("/boss2x", response_model = boss2x_schema.Boss2x)
def boss2x(db: Session = Depends(get_db)):
    return db.query(Boss2x).get(1)

@router.put("/boss2x/update")
def boss2x_update(db: Session = Depends(get_db)):
    db_boss2x = db.query(Boss2x).get(1)
    db_boss2x.active = not db_boss2x.active
    db.add(db_boss2x)
    db.commit()