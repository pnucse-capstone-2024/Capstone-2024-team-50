import json

import os

from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import Session

from core.config import settings

from model.database import engine, get_db, Base

from model.record import models as record_models
from model.record import schemas as record_schemas
from model.record import crud as record_crud

PATH = os.path.abspath(os.pardir)

def init_database(engine: engine, db: Annotated[Session, Depends(get_db)]):
    # Create Tables
    Base.metadata.create_all(bind=engine)

    # Create Test Record if not exists
    test_record = record_crud.get_test_records(db)

    if not test_record:
        test_record = record_schemas.TestRecordCreate(
            uid=1,
            name='first test record',
        )

        record_crud.create_test_record(db, test_record)

        test_record2 = record_schemas.TestRecordCreate(
            uid=2,
            name='test record2',
        )

        record_crud.create_test_record(db, test_record2)

        test_record3 = record_schemas.TestRecordCreate(
            uid=1,
            name='tttest record2',
        )

        record_crud.create_test_record(db, test_record3)

