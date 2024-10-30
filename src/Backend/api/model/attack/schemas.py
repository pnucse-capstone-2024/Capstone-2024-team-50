from pydantic import BaseModel
from typing import List, Optional

class TacticsBase(BaseModel):
    taid: str
    name: str
    description: Optional[str] = None

class TacticsCreate(TacticsBase):
    pass

class Tactics(TacticsBase):
    id: int
    techniques: List['Techniques'] = []
    attacks: List['Attacks'] = []

    class Config:
        orm_mode = True

class TechniquesBase(BaseModel):
    tid: str
    name: str
    description: Optional[str] = None
    taid: str

class TechniquesCreate(TechniquesBase):
    pass

class Techniques(TechniquesBase):
    id: int
    commands: List['Commands'] = []
    attacks: List['Attacks'] = []

    class Config:
        orm_mode = True

class CommandsBase(BaseModel):
    platform: str
    shell_type: str
    command: str
    cleanup: Optional[str] = None
    save_to: List[str]
    requirements: List[str]
    attack_id: int

class CommandsCreate(CommandsBase):
    pass

class Commands(CommandsBase):
    id: int
    payloads: List['Payloads'] = []
    attack: Optional['Attacks'] = None

    class Config:
        orm_mode = True

class PayloadsBase(BaseModel):
    filename: str
    command_id: int

class PayloadsCreate(PayloadsBase):
    pass

class Payloads(PayloadsBase):
    id: int
    command: Optional['Commands'] = None

    class Config:
        orm_mode = True

class AttacksBase(BaseModel):
    name: str
    description: Optional[str] = None
    tid: str

class AttacksCreate(AttacksBase):
    pass

class Attacks(AttacksBase):
    id: int
    techniques: Techniques
    commands: List['Commands'] = []

    class Config:
        orm_mode = True

class CVEAttacksBase(BaseModel):
    cve_id: str
    cve_platform: str
    cve_command: str
    cve_title: str
    cve_description: Optional[str] = None
    cve_tid: List[str]
    cve_mitigation: Optional[str] = None

class CVEAttacksCreate(CVEAttacksBase):
    pass

class CVEAttacks(CVEAttacksBase):
    id: int
    techniques: List['Techniques'] = []

    class Config:
        orm_mode = True

class ScenarioBase(BaseModel):
    name: str
    description: Optional[str] = None
    attack_names: List[str]

class ScenarioCreate(ScenarioBase):
    pass

class Scenario(ScenarioBase):
    id: int
    attacks: List['Attacks']

    class Config:
        orm_mode = True

class ScenarioUpdate(ScenarioBase):
    pass