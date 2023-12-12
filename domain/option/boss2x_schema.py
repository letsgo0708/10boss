from pydantic import BaseModel

class Boss2x(BaseModel):
    id: int
    active: bool


    class Config:
        orm_mode = True
