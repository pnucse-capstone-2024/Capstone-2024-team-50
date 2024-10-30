from datetime import datetime

from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas

def get_test_records(db: Session):
    return db.query(models.TestRecord).all()

def create_test_record(db: Session, test_record: schemas.TestRecordCreate):
    db_test_record = models.TestRecord(uid=test_record.uid, name=test_record.name, date=datetime.utcnow())
    db.add(db_test_record)
    db.commit()
    db.refresh(db_test_record)
    return db_test_record

def get_test_records_by_uid(db: Session, uid: int) -> List[models.TestRecord]:
    return db.query(models.TestRecord).filter(models.TestRecord.uid == uid).all()

def get_test_records_by_id(db: Session, id: int) -> models.TestRecord:
    return db.query(models.TestRecord).filter(models.TestRecord.id == id).first()
