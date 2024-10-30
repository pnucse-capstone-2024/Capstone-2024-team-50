from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.attack import schemas as attack_schemas
from model.attack import crud as attack_crud

router = APIRouter(
    prefix='/cve',
    tags=['cve'],
    responses={404: {'description': 'Not Found'}},
)

@router.get('/allcve')
def get_cve(db: Annotated[Session, Depends(get_db)]):
    return attack_crud.get_cve(db)

@router.post('/cve')
def get_cve_by_id(id: List[int], db: Annotated[Session, Depends(get_db)]):
    return attack_crud.get_cve_by_id(db, id)