from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

router = APIRouter(
    prefix='/test',
    tags=['test'],
    responses={404: {'description': 'Not Found'}},
)

@router.post('/me')
async def post_test(Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]) :

    print("success")

    return {'result': 'success'}