from datetime import datetime
from pydantic import BaseModel


class AgentBase(BaseModel):
    uid: int
    hostname: str
    ip: str
    os: str
    connected: bool

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: int
    last_checkin: datetime

    class Config:
        orm_mode = True

class AgentUpdate(AgentBase):
    last_checkin: datetime
    pass

class AgentPrepareBase(BaseModel):
    agent_id: int
    commands: list
    real_commands: list
    payloads: list
    status: str

class AgentPrepareCreate(AgentPrepareBase):
    pass

class AgentPrepare(AgentPrepareBase):
    id: int

    class Config:
        orm_mode = True

class AgentPrepareUpdate(AgentPrepareBase):
    pass