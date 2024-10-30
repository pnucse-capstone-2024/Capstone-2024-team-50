from datetime import datetime
from sqlalchemy import Column, BigInteger,  String, Boolean, DateTime, ForeignKey, ARRAY, JSON
from sqlalchemy.orm import relationship

from model.database import Base


class Result(Base):
    __tablename__ = 'results'

    id = Column(BigInteger, primary_key=True, index=True)
    agent_id = Column(BigInteger, ForeignKey('agent.id'))
    tids = Column(ARRAY(String))
    cmd_ids = Column(ARRAY(BigInteger))
    attack_ids = Column(ARRAY(BigInteger))

class CommandResult(Base):
    __tablename__ = 'command_results'

    id = Column(BigInteger, primary_key=True, index=True)
    agent_id = Column(BigInteger, ForeignKey('agent.id'))
    input_command = Column(String)
    output_command = Column(String, nullable=True)
    success = Column(Boolean, default=False)
    attack_id = Column(BigInteger, ForeignKey('attacks.id'))
    value = Column(ARRAY(String), nullable=True)

class HostInfo(Base):
    __tablename__ = 'host_info'

    id = Column(BigInteger, primary_key=True, index=True)
    agent_id = Column(BigInteger, ForeignKey('agent.id'))
    host_dir_staged = Column(String, nullable=True)
    host_file_path = Column(String, nullable=True)
    host_dir_compress = Column(String, nullable=True)
    host_file_name = Column(String, nullable=True)
    wifi_network_ssid = Column(String, nullable=True)
    host_user_name = Column(String, nullable=True)
    domain_user_name = Column(String, nullable=True)
    remote_execution_smb = Column(String, nullable=True)