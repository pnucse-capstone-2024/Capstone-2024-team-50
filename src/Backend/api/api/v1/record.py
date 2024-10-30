from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.record import schemas as record_schemas
from model.record import crud as record_crud


router = APIRouter(
    prefix='/record',
    tags=['record'],
    responses={404: {'description': 'Not Found'}},
)

@router.get('/get')
def get_test_records(db: Annotated[Session, Depends(get_db)]):
    return record_crud.get_test_records(db)

@router.get('/get/{uid}')
def get_test_records_by_uid(uid: int, db: Annotated[Session, Depends(get_db)]):
    return record_crud.get_test_records_by_uid(db, uid)


@router.get('/get/id/{id}')
def get_test_records_by_id(id: int, db: Annotated[Session, Depends(get_db)]):
    
    return record_crud.get_test_records_by_id(db, id).cve_result
