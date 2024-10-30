from datetime import datetime

from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas

from model.attack import crud as attack_crud
from model.attack import schemas as attack_schemas

from model.agent import crud as agent_crud
from model.agent import schemas as agent_schemas
from sqlalchemy.orm.attributes import flag_modified
def get_command_results(db: Session, aid: int) -> List[schemas.CommandResult]:
    return db.query(models.CommandResult).filter(models.CommandResult.agent_id == aid).all()

def get_command_result_by_command(db: Session, aid: int, input_command: str) -> Optional[schemas.CommandResult]:
    return db.query(models.CommandResult).filter(models.CommandResult.agent_id == aid, models.CommandResult.input_command == input_command).first()

def get_command_results_by_tid(db: Session, tid: str, uid: int) -> List[schemas.CommandResult]:
    attacks = attack_crud.get_attacks_by_tid(db, tid)

    if not attacks:
        return []
    
    attack_ids = [attack.id for attack in attacks]
    
    agents = agent_crud.get_agents(db, uid)

    if not agents:
        return []
    
    agent_ids = [agent.id for agent in agents]

    command_results_by_attack_id_and_agent_id = db.query(models.CommandResult).filter(models.CommandResult.attack_id.in_(attack_ids), models.CommandResult.agent_id.in_(agent_ids)).all()

    if not command_results_by_attack_id_and_agent_id:
        return []
    
    return command_results_by_attack_id_and_agent_id

def get_command_results_by_attack_ids(db: Session, attack_ids: List[int], aid: int) -> List[schemas.CommandResult]:
    return db.query(models.CommandResult).filter(models.CommandResult.attack_id.in_(attack_ids), models.CommandResult.agent_id == aid).all()

def create_command_result(db: Session, command_result: schemas.CommandResultCreate) -> schemas.CommandResult:
    db_command_result = models.CommandResult(**command_result.dict())
    db.add(db_command_result)
    db.commit()
    db.refresh(db_command_result)
    return db_command_result

def update_command_result_output(db: Session, crid: int, command_result: schemas.CommandResultUpdate) -> Optional[schemas.CommandResult]:
    db_command_result = db.query(models.CommandResult).filter(models.CommandResult.id == crid).first()
    if db_command_result:
        db_command_result.output_command = command_result.output_command
        db.commit()
        db.refresh(db_command_result)
        return db_command_result
    return None

def get_scenario_success_by_aid(db: Session, aid: int) -> bool:
    attack_scenarios = attack_crud.get_scenarios(db)

    success_scenarios = []

    if not attack_scenarios:
        return False
    
    for attack_scenario in attack_scenarios:
        attack_names = attack_scenario.attack_names
        attack_ids = [attack_crud.get_attack_id_by_name(db, attack_name) for attack_name in attack_names]
        success_command_results = []

        for attack_id in attack_ids:
            command_results = db.query(models.CommandResult).filter(models.CommandResult.attack_id == attack_id, models.CommandResult.agent_id == aid, models.CommandResult.success == True).all()
            if not command_results:
                break
            for command_result in command_results:
                if command_result.success:
                    success_command_results.append(command_result)
                    break

        if not success_command_results:
            continue

        if len(success_command_results) == len(attack_ids):
            attacks = attack_crud.get_attacks_by_ids(db, attack_ids)
            # 기존 attack_scenario에 attacks를 추가
            # 근데 attack_names의 순서를 따라가야함
            # attack_descriptions = []
            # for attack in attacks:
            #     attack_descriptions.append(attack.description)

            attack_descriptions = [attacks[i].description for i in range(len(attacks))]
            attack_scenario.descriptions = attack_descriptions
            attack_scenario.attack_ids = attack_ids
            attack_input_commands = [success_command_result.input_command for success_command_result in success_command_results]
            attack_scenario.input_commands = attack_input_commands
            attack_output_commands = [success_command_result.output_command for success_command_result in success_command_results]
            attack_scenario.output_commands = attack_output_commands
            
            success_scenarios.append(attack_scenario)


        
    if success_scenarios:
        return success_scenarios
    
def get_host_info(db: Session, aid: int) -> List[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()


def create_host_info(db: Session, host_info: schemas.HostInfoCreate) -> schemas.HostInfo:
    db_host_info = models.HostInfo(**host_info.dict())
    db.add(db_host_info)
    db.commit()
    db.refresh(db_host_info)
    return db_host_info

    # host_dir_staged = Column(String, nullable=True)
    # host_file_path = Column(String, nullable=True)
    # host_dir_compress = Column(String, nullable=True)
    # host_file_name = Column(String, nullable=True)
    # wifi_network_ssid = Column(String, nullable=True)
    # host_user_name = Column(String, nullable=True)
    # domain_user_name = Column(String, nullable=True)

def get_host_dir_staged(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().host_dir_staged

def get_host_file_path(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().host_file_path

def get_host_dir_compress(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().host_dir_compress

def get_host_file_name(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().host_file_name

def get_wifi_network_ssid(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().wifi_network_ssid

def get_host_user_name(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().host_user_name

def get_domain_user_name(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().domain_user_name

def get_remote_execution_smb(db: Session, aid: int) -> Optional[schemas.HostInfo]:
    return db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first().remote_execution_smb

def update_host_dir_staged(db: Session, aid: int, host_dir_staged: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.host_dir_staged = host_dir_staged
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None

def update_host_file_path(db: Session, aid: int, host_file_path: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.host_file_path = host_file_path
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None

def update_host_dir_compress(db: Session, aid: int, host_dir_compress: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.host_dir_compress = host_dir_compress
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None

def update_host_file_name(db: Session, aid: int, host_file_name: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.host_file_name = host_file_name
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None

def update_wifi_network_ssid(db: Session, aid: int, wifi_network_ssid: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.wifi_network_ssid = wifi_network_ssid
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None

def update_host_user_name(db: Session, aid: int, host_user_name: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.host_user_name = host_user_name
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None

def update_domain_user_name(db: Session, aid: int, domain_user_name: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.domain_user_name = domain_user_name
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None

def update_remote_execution_smb(db: Session, aid: int, remote_execution_smb: str) -> Optional[schemas.HostInfo]:
    db_host_info = db.query(models.HostInfo).filter(models.HostInfo.agent_id == aid).first()
    if db_host_info:
        db_host_info.remote_execution_smb = remote_execution_smb
        db.commit()
        db.refresh(db_host_info)
        return db_host_info
    return None