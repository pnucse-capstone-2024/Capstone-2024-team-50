from pydantic import BaseModel
from typing import List, Optional

class CVEResultBase(BaseModel):
    rid: int
    cid: int
    is_success: bool

class CVEResultCreate(CVEResultBase):
    pass

class CVEResult(CVEResultBase):
    id: int
    test_record: List['TestRecord'] = []
    cve_attacks: List['CVEAttacks'] = []

    class Config:
        orm_mode = True