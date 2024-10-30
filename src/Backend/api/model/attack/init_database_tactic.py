from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import Session

from core.config import settings

from model.database import engine, get_db, Base

from model.attack import schemas
from model.attack import crud
from model.attack import models

def init_database(engine: engine, db: Annotated[Session, Depends(get_db)]):
    Base.metadata.create_all(bind=engine)

    # Create Tactics
    tactics = crud.get_tactics(db)
    if not tactics:
        ta1 = schemas.TacticsCreate(taid='TA0043', name='Reconnaissance', description='Gathering information about targets')
        ta2 = schemas.TacticsCreate(taid='TA0042', name='Resource Development', description='Developing resources for future actions')
        ta3 = schemas.TacticsCreate(taid='TA0001', name='Initial Access', description='Gaining a foothold in the network')
        ta4 = schemas.TacticsCreate(taid='TA0002', name='Execution', description='Executing malicious code')
        ta5 = schemas.TacticsCreate(taid='TA0003', name='Persistence', description='Maintaining access to the network')
        ta6 = schemas.TacticsCreate(taid='TA0004', name='Privilege Escalation', description='Gaining higher privileges')
        ta7 = schemas.TacticsCreate(taid='TA0005', name='Defense Evasion', description='Avoiding detection')
        ta8 = schemas.TacticsCreate(taid='TA0006', name='Credential Access', description='Stealing credentials')
        ta9 = schemas.TacticsCreate(taid='TA0007', name='Discovery', description='Discovering information about the network')
        ta10 = schemas.TacticsCreate(taid='TA0008', name='Lateral Movement', description='Moving laterally within the network')
        ta11 = schemas.TacticsCreate(taid='TA0009', name='Collection', description='Gathering information')
        ta12 = schemas.TacticsCreate(taid='TA0011', name='Command and Control', description='Controlling compromised systems')
        ta13 = schemas.TacticsCreate(taid='TA0010', name='Exfiltration', description='Stealing information')
        ta14 = schemas.TacticsCreate(taid='TA0040', name='Impact', description='Damaging the network')

        crud.create_tactic(db, ta1)
        crud.create_tactic(db, ta2)
        crud.create_tactic(db, ta3)
        crud.create_tactic(db, ta4)
        crud.create_tactic(db, ta5)
        crud.create_tactic(db, ta6)
        crud.create_tactic(db, ta7)
        crud.create_tactic(db, ta8)
        crud.create_tactic(db, ta9)
        crud.create_tactic(db, ta10)
        crud.create_tactic(db, ta11)
        crud.create_tactic(db, ta12)
        crud.create_tactic(db, ta13)
        crud.create_tactic(db, ta14)