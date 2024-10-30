from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.CVEResult import schemas as cve_result_schemas
from model.CVEResult import crud as cve_result_crud


router = APIRouter(
    prefix='/cve_result',
    tags=['cve_result'],
    responses={404: {'description': 'Not Found'}},
)

@router.get('/get')
def get_cve_results(db: Annotated[Session, Depends(get_db)]):
    return cve_result_crud.get_cve_results(db)

@router.get('/get/{rid}')
def get_cve_results_by_rid(rid: int, db: Annotated[Session, Depends(get_db)]):
    return cve_result_crud.get_cve_results_by_rid(db, rid)

@router.get('/record/{rid}')
def get_cve_record_by_rid(rid: int, db: Annotated[Session, Depends(get_db)]):
    return cve_result_crud.get_cve_results_by_rid(db, rid).test_record

@router.get('/cve_attacks/{rid}')
def get_cve_attacks_by_rid(rid: int, db: Annotated[Session, Depends(get_db)]):
    return cve_result_crud.get_cve_attacks_by_rid(db, rid)
