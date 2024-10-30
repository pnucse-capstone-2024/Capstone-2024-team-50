from pydantic import BaseModel
from typing import List, Optional

class TestRecordBase(BaseModel):
    uid: int
    name: str

class TestRecordCreate(TestRecordBase):
    pass

class TestRecord(TestRecordBase):
    id: int

    class Config:
        orm_mode = True