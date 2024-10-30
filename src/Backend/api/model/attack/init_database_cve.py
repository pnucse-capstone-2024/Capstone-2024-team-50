from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import Session

from core.config import settings

from model.database import engine, get_db, Base

from model.attack import schemas
from model.attack import crud
from model.attack import models

CVE1_TITLE = 'Linux Kernel Privilege Escalation'
CVE2_TITLE = 'Log4Shell'
CVE3_TITLE = 'Dirty Pipe'

CVE1_DESCRIPTION = 'Escalation of root privileges using nf_tables.'
CVE2_DESCRIPTION = 'A vulnerability discovered in Log4j, a Java-based logging package. Allows attackers to execute code on remote servers (Remote Code Execution, RCE).'
CVE3_DESCRIPTION = 'Linux kernel vulnerability that allows the ability of non-privileged users to overwrite read-only files.'

CVE1_MITIGATION = 'If you are using Linux kernel version 3.15 ~ 6.1.76 / 6.2 ~ 6.6.15 / 6.7 ~ 6.7.3, update the kernel to the latest version'
CVE2_MITIGATION = 'Log4j 2.15.0 has been released to address the vulnerability'
CVE3_MITIGATION = 'If you are running a Linux kernel version 5.8 or higher, you should patch your kernel to 5.16.11, 5.15.25 and 5.10.102 or greater.'

def init_database(engine: engine, db: Annotated[Session, Depends(get_db)]):
    Base.metadata.create_all(bind=engine)

    # Create CVE List
    cve = crud.get_cve(db)
    if not cve:
        cve1 = schemas.CVEAttacksCreate(cve_id='CVE 2024-1086', cve_platform='Linux', cve_command='./exploit', cve_title=CVE1_TITLE, cve_description=CVE1_DESCRIPTION, cve_tid=['T1068', 'T1543', 'T1547', 'T1059', 'T1203'], cve_mitigation=CVE1_MITIGATION)
        cve2 = schemas.CVEAttacksCreate(cve_id='CVE 2021-44228', cve_platform='Linux', cve_command='./exploit', cve_title=CVE2_TITLE, cve_description=CVE2_DESCRIPTION, cve_tid=['T1190', 'T1059', 'T1203', 'T1068', 'T1105', 'T1071'], cve_mitigation=CVE2_MITIGATION)
        cve3 = schemas.CVEAttacksCreate(cve_id='CVE 2022-0847', cve_platform='Linux', cve_command='./exploit', cve_title=CVE3_TITLE, cve_description=CVE3_DESCRIPTION , cve_tid=['T1106', 'T1068', 'T1548', 'T1070', 'T1005', 'T1556'], cve_mitigation=CVE3_MITIGATION)

        crud.create_cve(db, cve1)
        crud.create_cve(db, cve2)
        crud.create_cve(db, cve3)



