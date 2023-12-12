from models import Boss
from sqlalchemy.orm import Session

def get_boss_list(db: Session):
    boss_list = db.query(Boss).order_by(Boss.delay.desc()).all()
    return boss_list

def get_boss(db: Session, boss_id: int):
    boss = db.query(Boss).get(boss_id)
    return boss