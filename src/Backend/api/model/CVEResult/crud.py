from datetime import datetime

from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_cve_results(db: Session):
    return db.query(models.CVEResult).all()

def get_cve_results_by_rid(db: Session, rid: int):
    return db.query(models.CVEResult).filter(models.CVEResult.rid == rid).first()

def create_cve_result(db: Session, cve_result: schemas.CVEResultCreate):
    db_cve_result = models.CVEResult(rid=cve_result.rid, cid=cve_result.cid, is_success=cve_result.is_success)
    db.add(db_cve_result)
    db.commit()
    db.refresh(db_cve_result)
    return db_cve_result

def get_cve_attacks_by_rid(db: Session, rid: int):
    return db.query(models.CVEResult).filter(models.CVEResult.rid == rid).first().cve_attacks
