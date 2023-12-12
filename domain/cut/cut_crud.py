from sqlalchemy.orm import Session
from domain.cut.cut_schema import CutCreate
from models import Boss, Cut
from datetime import datetime, timedelta

def create_cut(db: Session, boss: Boss, cut_create: CutCreate, boss2x: bool):
    cut_time_tmp = datetime.strptime(str(cut_create.cut_time), '%H%M') # 네자리 숫자로 입력된 문자열을 시간:분(24시간제)으로 변환
    cut_time_final = datetime.combine(datetime.now().date(), cut_time_tmp.time()) # 입력시점 날짜와 결합
    if boss2x:
        gen_time = cut_time_final + timedelta(hours=boss.delay)/2 # 보스 주기만큼 더해서 젠시간 예상
    else:
        gen_time = cut_time_final + timedelta(hours=boss.delay)
    if datetime.now() < gen_time - timedelta(hours=16): # 간혹 0시~1시 사이에 전날 23시~24시 사이 컷 기록 입력하는 경우 순서 꼬이는걸 방지하기 위함
        gen_time = gen_time - timedelta(hours=24)
    db_cut = Cut(boss=boss, cut_time=cut_create.cut_time, gen_time=gen_time, create_time=datetime.now()) # db 작성하여 추가
    db.add(db_cut)
    db.commit()

def get_cut_list(db: Session):
    cut_list = db.query(Cut).order_by(Cut.gen_time.desc()).all()
    return cut_list

def get_cut(db: Session, cut_id: int):
    db_cut = db.query(Cut).get(cut_id)
    return db_cut

def delete_cut(db: Session, db_cut: Cut):
    db.delete(db_cut)
    db.commit()

def delete_cut_all(db: Session):
    for i in db.query(Cut).all():
        db.delete(i)
    db.commit()
