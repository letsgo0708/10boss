from pydantic import BaseModel
from domain.cut.cut_schema import Cut

class Boss(BaseModel):
    id: int
    name : str
    name_kr : str
    delay : int
    cuts : list[Cut] = []

    class Config:
        orm_mode = True
