import yaml
import os
import glob

from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import Session

from core.config import settings

from model.database import engine, get_db, Base

from model.attack import schemas
from model.attack import crud

def get_yaml_files(directory):
    pattern = os.path.join(directory, '**', '*.yml') 
    return glob.glob(pattern, recursive=True)

current_dir = os.path.dirname(__file__)

yaml_files = get_yaml_files(os.path.join(current_dir, 'attacks'))

def load_scenario_files(directory):
    pattern = os.path.join(directory, '*.yml') 
    return glob.glob(pattern, recursive=True)

scenario_files = load_scenario_files(os.path.join(current_dir, 'scenarios'))

def load_yaml(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)
    
def add_technique(data, taid, db):
    tid=data['technique']['attack_id']
    
    t_check = crud.get_technique_by_tid(db, tid)
    if t_check:
        return t_check
    
    technique = schemas.TechniquesCreate(
        tid=tid,
        name=data['technique']['name'],
        # description=data['description'],
        taid=taid
    )
    technique = crud.create_technique(db, technique)
    
    return technique

def add_attack(data, technique, db):
    attack = schemas.AttacksCreate(
        name=data['name'],
        description=data['description'],
        tid=technique.tid
    )
    return crud.create_attack(db, attack)

def add_commands(data, attack, db):
    platforms = data.get('platforms', {})
    requirements = data.get('requirements', [])
    commands = []
    for platform, shells in platforms.items():
        for shell_type, shell_data in shells.items():
            if shell_data.get('command') is None:
                continue
            command = schemas.CommandsCreate(
                platform=platform,
                shell_type=shell_type,
                command=shell_data['command'],
                cleanup=shell_data.get('cleanup', ''),
                save_to=shell_data.get('save_to', []),
                requirements=requirements,
                attack_id=attack.id
            )
            commands.append(crud.create_command(db, command))
    print(commands)
    return commands

def add_payloads(data, commands, db):
    platforms = data.get('platforms', {})
    for platform, shells in platforms.items():
        for shell_type, shell_data in shells.items():
            payloads = shell_data.get('payloads', [])
            for filename in payloads:
                for command in commands:
                    if command.platform == platform and command.shell_type == shell_type:
                        payload = schemas.PayloadsCreate(
                            filename=filename,
                            command_id=command.id
                        )
                        crud.create_payload(db, payload)


def add_scenarios(data, db):
    for scenario in data:
        attack_names = scenario['attack_names']
        scenario = schemas.ScenarioCreate(
            name=scenario['name'],
            description=scenario['description'],
            attack_names=attack_names
        )
        crud.create_scenario(db, scenario)

def init_database(engine: engine, db: Annotated[Session, Depends(get_db)]):
    Base.metadata.create_all(bind=engine)
    
    tmp = crud.get_techniques(db)
    if not tmp:
        for file in yaml_files:
            yaml_data = load_yaml(file)
            for data in yaml_data:    
                taid = file.split('/')[-2]
                technique = add_technique(data, taid, db)
                attack = add_attack(data, technique, db)
                commands = add_commands(data, attack, db)
                add_payloads(data, commands, db)

    tmp = crud.get_scenarios(db)
    if not tmp:
        for file in scenario_files:
            yaml_data = load_yaml(file)
            add_scenarios(yaml_data, db)