from datetime import datetime

from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas

from model.result import crud as result_crud
from model.result import schemas as result_schemas
from model.result import models as result_models

def get_all_agents(db: Session) -> List[schemas.Agent]:
    return db.query(models.Agent).all()

def get_all_agents_connected(db: Session) -> List[schemas.Agent]:
    return db.query(models.Agent).filter(models.Agent.connected == True).all()

def get_agents(db: Session, uid: int) -> List[schemas.Agent]:
    return db.query(models.Agent).filter(models.Agent.uid == uid).all()

def get_agent(db: Session, aid: int) -> Optional[schemas.Agent]:
    return db.query(models.Agent).filter(models.Agent.id == aid).first()

def get_agent_by_hostname(db: Session, hostname: str) -> Optional[schemas.Agent]:
    return db.query(models.Agent).filter(models.Agent.hostname == hostname).first()

def get_agent_by_hostname_with_uid(db: Session, hostname: str, uid: int) -> Optional[schemas.Agent]:
    return db.query(models.Agent).filter(models.Agent.hostname == hostname, models.Agent.uid == uid).first()

def get_agent_by_hostname_with_uid_and_os(db: Session, hostname: str, uid: int, os: str) -> Optional[schemas.Agent]:
    return db.query(models.Agent).filter(models.Agent.hostname == hostname, models.Agent.uid == uid, models.Agent.os == os).first()

def create_agent(db: Session, agent: schemas.AgentCreate) -> schemas.Agent:
    db_agent = models.Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def update_agent(db: Session, aid: int, agent: schemas.AgentUpdate) -> Optional[schemas.Agent]:
    db_agent = db.query(models.Agent).filter(models.Agent.id == aid).first()
    if db_agent:
        db_agent.hostname = agent.hostname
        db_agent.ip = agent.ip
        db_agent.os = agent.os
        db_agent.connected = agent.connected
        db_agent.last_checkin = datetime.now()
        db.commit()
        db.refresh(db_agent)
        return db_agent
    return None

def update_agent_connected(db: Session, aid: int, connected: bool) -> Optional[schemas.Agent]:
    db_agent = db.query(models.Agent).filter(models.Agent.id == aid).first()
    if db_agent:
        db_agent.connected = connected
        db.commit()
        db.refresh(db_agent)
        return db_agent
    return None

def delete_agent(db: Session, aid: int) -> Optional[schemas.Agent]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        db.delete(db_agent_prepare)
        db.commit()

    db_command_result = db.query(result_models.CommandResult).filter(result_models.CommandResult.agent_id == aid).all()
    if db_command_result:
        for command_result in db_command_result:
            db.delete(command_result)
        db.commit()

    db_host_info = db.query(result_models.HostInfo).filter(result_models.HostInfo.agent_id == aid).all()
    if db_host_info:
        for host_info in db_host_info:
            db.delete(host_info)
        db.commit()    

    db_agent = db.query(models.Agent).filter(models.Agent.id == aid).first()
    if db_agent:
        db.delete(db_agent)
        db.commit()
        return db_agent
    return None

def count_agents(db: Session, uid: int) -> int:
    return db.query(models.Agent).filter(models.Agent.uid == uid).count()

def create_agent_prepare(db: Session, agent_prepare: schemas.AgentPrepareCreate) -> schemas.AgentPrepare:
    db_agent_prepare = models.AgentPrepare(**agent_prepare.dict())
    db.add(db_agent_prepare)
    db.commit()
    db.refresh(db_agent_prepare)
    return db_agent_prepare

def get_agent_prepare(db: Session, aid: int) -> Optional[schemas.AgentPrepare]:
    return db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()

def get_agent_prepare_status(db: Session, aid: int) -> Optional[str]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        return db_agent_prepare.status
    return None

def get_agent_prepare_commands(db: Session, aid: int) -> Optional[List[str]]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        return db_agent_prepare.commands
    return None

def get_agent_prepare_payloads(db: Session, aid: int) -> Optional[List[str]]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        return db_agent_prepare.payloads
    return None

def get_agent_prepare_real_commands(db: Session, aid: int) -> Optional[List[str]]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        return db_agent_prepare.real_commands
    return None

def update_agent_prepare_status_to_prepare(db: Session, aid: int) -> Optional[schemas.AgentPrepare]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        db_agent_prepare.status = 'prepare'
        db.commit()
        db.refresh(db_agent_prepare)
        return db_agent_prepare
    return None

def update_agent_prepare_status_to_proceed(db: Session, aid: int) -> Optional[schemas.AgentPrepare]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        db_agent_prepare.status = 'proceed'
        db.commit()
        db.refresh(db_agent_prepare)
        return db_agent_prepare
    return None

def update_agent_prepare_status_to_finish(db: Session, aid: int) -> Optional[schemas.AgentPrepare]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        db_agent_prepare.status = 'finish'
        db.commit()
        db.refresh(db_agent_prepare)
        return db_agent_prepare
    return None

def update_agent_prepare_commands_and_payloads(db: Session, aid: int, real_commands: List[str], commands: List[str], payloads: List[str]) -> Optional[schemas.AgentPrepare]:
    db_agent_prepare = db.query(models.AgentPrepare).filter(models.AgentPrepare.agent_id == aid).first()
    if db_agent_prepare:
        db_agent_prepare.real_commands = real_commands
        db_agent_prepare.commands = commands
        db_agent_prepare.payloads = payloads
        db.commit()
        db.refresh(db_agent_prepare)
        return db_agent_prepare
    return None