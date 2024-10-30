from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.user import schemas as user_schemas
from model.user import crud as user_crud

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/me', response_model=user_schemas.User)
async def get_me(Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    user = user_crud.get_user(db, current_user)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return user


@router.put('/me', response_model=user_schemas.User)
async def update_me(user: user_schemas.UserUpdate, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    user = user_crud.update_user(db, current_user, user)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return user


@router.put('/me/password', response_model=user_schemas.User)
async def update_me_password(user: user_schemas.UserPasswordUpdate, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]):
    Authorize.fresh_jwt_required()

    current_user = Authorize.get_jwt_subject()

    user = user_crud.update_user_password(db, current_user, user)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return user

@router.put('/update')
async def update_user(user: user_schemas.UserInfoUpdate, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]):
    db_user = user_crud.get_user(db, user.uid)

    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')

    try:
        user_crud.update_user_info(db, user.uid, user.username, user.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail="update user info error")

    return { "msg": "update user info success" }