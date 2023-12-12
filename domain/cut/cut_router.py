from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.cut import cut_schema, cut_crud
from domain.boss import boss_crud
from domain.option import boss2x_router

router = APIRouter(
    prefix="/api/cut",
)

@router.get("/list", response_model = list[cut_schema.Cut])
def cut_list(db: Session = Depends(get_db)):
    _cut_list = cut_crud.get_cut_list(db)
    return _cut_list

@router.get("/detail/{cut_id}", response_model = cut_schema.Cut)
def cut_detail(cut_id: int, db: Session = Depends(get_db)):
    cut = cut_crud.get_cut(db, cut_id=cut_id)
    return cut

@router.post("/create/{boss_id}", status_code=status.HTTP_204_NO_CONTENT)
def cut_create(boss_id: int, _cut_create: cut_schema.CutCreate, db: Session = Depends(get_db)):
    boss = boss_crud.get_boss(db, boss_id=boss_id)
    boss2x = boss2x_router.boss2x(db)
    if not boss:
        raise HTTPException(status_code=404, detail="Boss not found")
    cut_crud.create_cut(db, boss=boss, cut_create=_cut_create, boss2x=boss2x.active)

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def cut_delete(_cut_delete: cut_schema.CutDelete, db: Session = Depends(get_db)):
    db_cut = cut_crud.get_cut(db, cut_id=_cut_delete.cut_id)
    if not db_cut:
        raise HTTPException(status_code=404, detail="Cut not found")
    cut_crud.delete_cut(db, db_cut=db_cut)

@router.delete("/delete_all", status_code=status.HTTP_204_NO_CONTENT)
def cut_delete_all(db: Session = Depends(get_db)):
    cut_crud.delete_cut_all(db)

