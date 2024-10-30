from datetime import datetime

from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas

def get_tactics(db: Session):
    return db.query(models.Tactics).order_by(models.Tactics.id).all()

def create_tactic(db: Session, tactic: schemas.TacticsCreate):
    db_tactic = models.Tactics(name=tactic.name, taid=tactic.taid, description=tactic.description)
    db.add(db_tactic)
    db.commit()
    db.refresh(db_tactic)
    return db_tactic

def get_techniques(db: Session):
    return db.query(models.Techniques).all()

def get_technique_by_tid(db: Session, tid: str):
    return db.query(models.Techniques).filter(models.Techniques.tid == tid).first()

def create_technique(db: Session, technique: schemas.TechniquesCreate):
    db_technique = models.Techniques(name=technique.name, tid=technique.tid, description=technique.description, taid=technique.taid)
    db.add(db_technique)
    db.commit()
    db.refresh(db_technique)
    return db_technique

def get_commands(db: Session):
    return db.query(models.Commands).all()

def get_command_by_command(db: Session, command: str):
    return db.query(models.Commands).filter(models.Commands.command == command).first()

def get_command_by_attack_id_and_platform_and_shell_type(db: Session, attack_id: int, platform: str, shell_type: str):
    return db.query(models.Commands).filter(models.Commands.attack_id == attack_id, models.Commands.platform == platform, models.Commands.shell_type == shell_type).first()

def create_command(db: Session, command: schemas.CommandsCreate):
    db_command = models.Commands(platform=command.platform, shell_type=command.shell_type, command=command.command, cleanup=command.cleanup, save_to=command.save_to, requirements=command.requirements, attack_id=command.attack_id)
    db.add(db_command)
    db.commit()
    db.refresh(db_command)
    return db_command

def get_payloads(db: Session):
    return db.query(models.Payloads).all()

def get_payload_by_command_id(db: Session, command_id: int):
    return db.query(models.Payloads).filter(models.Payloads.command_id == command_id).first() 

def create_payload(db: Session, payload: schemas.PayloadsCreate):
    db_payload = models.Payloads(filename=payload.filename, command_id=payload.command_id)
    db.add(db_payload)
    db.commit()
    db.refresh(db_payload)
    return db_payload

def get_attacks(db: Session):
    return db.query(models.Attacks).all()

def get_attacks_by_ids(db: Session, ids: List[int]):
    db_attacks = []
    for id in ids:
        db_attack = db.query(models.Attacks).filter(models.Attacks.id == id).first()
        if db_attack:
            db_attacks.append(db_attack)
    return db_attacks

def get_attacks_by_tid(db: Session, tid: str):
    return db.query(models.Attacks).filter(models.Attacks.tid == tid).all()

def get_attack_id_by_name(db: Session, name: str):
    db_attack = db.query(models.Attacks).filter(models.Attacks.name == name).first()
    if db_attack:
        return db_attack.id
    return 1

def get_attack_id_by_commnad(db: Session, command: str):
    db_command = db.query(models.Commands).filter(models.Commands.command == command).first()
    if db_command:
        return db_command.attack_id
    return 1

def create_attack(db: Session, attack: schemas.AttacksCreate):
    db_attack = models.Attacks(name=attack.name, description=attack.description, tid=attack.tid)
    db.add(db_attack)
    db.commit()
    db.refresh(db_attack)
    return db_attack

def get_scenarios(db: Session):
    return db.query(models.Scenario).all()

def create_scenario(db: Session, scenario: schemas.ScenarioCreate):
    db_scenario = models.Scenario(name=scenario.name, description=scenario.description, attack_names=scenario.attack_names)
    db.add(db_scenario)
    db.commit()
    db.refresh(db_scenario)
    return db_scenario

def get_scenario_by_id(db: Session, id: int):
    return db.query(models.Scenario).filter(models.Scenario.id == id).first()

### cve
def get_cve(db: Session):
    return db.query(models.CVEAttacks).all()

def create_cve(db: Session, cve: schemas.CVEAttacksCreate):
    db_cve = models.CVEAttacks(cve_id=cve.cve_id, cve_platform=cve.cve_platform, cve_command=cve.cve_command, cve_title=cve.cve_title, cve_description=cve.cve_description, cve_tid=cve.cve_tid, cve_mitigation=cve.cve_mitigation)
    db.add(db_cve)
    db.commit()
    db.refresh(db_cve)
    return db_cve

def get_cve_by_id(db: Session, id: List[int]):
    return db.query(models.CVEAttacks).filter(models.CVEAttacks.id.in_(id)).all()