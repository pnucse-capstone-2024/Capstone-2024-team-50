from datetime import datetime
from sqlalchemy import Column, BigInteger,  String, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from model.database import Base


class Agent(Base):
    __tablename__ = 'agent'

    id = Column(BigInteger, primary_key=True, index=True)
    uid = Column(BigInteger, ForeignKey('users.uid'))
    hostname = Column(String, index=True)
    ip = Column(String, index=True)
    os = Column(String)
    last_checkin = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    connected = Column(Boolean, default=False)    # True: connected, False: disconnected

class AgentPrepare(Base):
    __tablename__ = 'agent_prepare'

    id = Column(BigInteger, primary_key=True, index=True)
    agent_id = Column(BigInteger, ForeignKey('agent.id'))
    commands = Column(ARRAY(String), nullable=True)
    real_commands = Column(ARRAY(String), nullable=True)
    payloads = Column(ARRAY(String), nullable=True)
    status = Column(String, default='prepare')  # prepare, proceed, finish