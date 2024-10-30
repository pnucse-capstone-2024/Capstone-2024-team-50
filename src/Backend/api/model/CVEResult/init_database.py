import json

import os

from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import Session

from core.config import settings

from model.database import engine, get_db, Base

from model.CVEResult import models as cve_result_models
from model.CVEResult import schemas as cve_result_schemas
from model.CVEResult import crud as cve_result_crud

PATH = os.path.abspath(os.pardir)

def init_database(engine: engine, db: Annotated[Session, Depends(get_db)]):
    # Create Tables
    Base.metadata.create_all(bind=engine)

    # Create CVE Result if not exists
    cve_results = cve_result_crud.get_cve_results(db)

    if not cve_results:
        cve_result1 = cve_result_schemas.CVEResultCreate(
            rid=1,
            cid=1,
            is_success=True,
        )

        cve_result_crud.create_cve_result(db, cve_result1)

        cve_result2 = cve_result_schemas.CVEResultCreate(
            rid=1,
            cid=2,
            is_success=True,
        )

        cve_result_crud.create_cve_result(db, cve_result2)

        cve_result3 = cve_result_schemas.CVEResultCreate(
            rid=2,
            cid=1,
            is_success=False,
        )

        cve_result_crud.create_cve_result(db, cve_result3)