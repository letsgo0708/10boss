from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.boss import boss_crud, boss_schema

router = APIRouter(
    prefix="/api/boss",
)


@router.get("/list", response_model = list[boss_schema.Boss])
def boss_list(db: Session = Depends(get_db)):
    _boss_list = boss_crud.get_boss_list(db)
    return _boss_list
#
@router.get("/detail/{boss_id}", response_model=boss_schema.Boss)
def boss_detail(boss_id: int, db: Session = Depends(get_db)):
    boss = boss_crud.get_boss(db, boss_id=boss_id)
    return boss


