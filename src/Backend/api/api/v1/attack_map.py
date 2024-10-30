from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

import string

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.attack import schemas as attack_schemas
from model.attack import crud as attack_crud


router = APIRouter(
    prefix='/attack-map',
    tags=['attack-map'],
    responses={404: {'description': 'Not Found'}},
)

@router.get('/tactics')
def get_tactics(db: Annotated[Session, Depends(get_db)]):
    return attack_crud.get_tactics(db)

@router.get('/techniques')
def get_techniques(db: Annotated[Session, Depends(get_db)]):
    return attack_crud.get_techniques(db)

@router.post('/commands')
def get_commands(db: Annotated[Session, Depends(get_db)]):
    return attack_crud.get_commands(db)

@router.post('/attacks')
def get_attacks(db: Annotated[Session, Depends(get_db)]):
    return attack_crud.get_attacks(db)