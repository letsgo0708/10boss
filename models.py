from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Boss(Base):
    __tablename__ = "boss"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    name_kr = Column(String, nullable=True)
    delay = Column(Integer, nullable=False)

class Cut(Base):
    __tablename__ = "cut"

    id = Column(Integer, primary_key=True)
    cut_time = Column(Integer, nullable=False)
    gen_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)
    boss_id = Column(Integer, ForeignKey("boss.id"))
    boss = relationship("Boss", backref="cuts")

class Boss2x(Base):
    __tablename__ = "boss2x"

    id = Column(Integer, primary_key=True)
    active = Column(Boolean, nullable=False, default=False)

