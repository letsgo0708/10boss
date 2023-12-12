from pydantic import BaseModel, field_validator
import datetime

class CutCreate(BaseModel):
    cut_time : str

    @field_validator('cut_time')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        elif not v.isdigit():
            raise ValueError('숫자만 입력하세요.')
        elif len(str(v)) != 4:
            raise ValueError('네 자리 숫자를 입력하세요.')
        elif int(v) > 2359:
            raise ValueError('2359 보다 작은 숫자를 입력하세요.')
        elif int(v[-2:]) > 59:
            raise ValueError('"분"은 59보다 큰 수를 입력할 수 없습니다.')
        return v

class Cut(BaseModel):
    id : int
    cut_time : int
    gen_time : datetime.datetime
    boss_id : int
    create_time : datetime.datetime

    class Config:
        orm_mode = True

class CutDelete(BaseModel):
    cut_id : int

    class Config:
        orm_mode = True