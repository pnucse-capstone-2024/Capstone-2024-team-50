from typing import Annotated

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT

from core.security import verify_password

from model.database import get_db

from model.user import crud as user_crud

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={404: {'description': 'Not found'}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/sign-in')


@router.post('/sign-in')
async def sign_in(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]):
    user = user_crud.get_user_by_username(db, form_data.username)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Incorrect password')

    user_claims = {
        'username': user.username,
        'is_admin': user.is_admin,
    }

    access_token = Authorize.create_access_token(
        subject=user.uid, user_claims=user_claims, fresh=True)
    refresh_token = Authorize.create_refresh_token(subject=user.uid)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)

    return {'msg': 'Signed in successfully'}


@router.post('/refresh')
async def refresh(Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()

    user = user_crud.get_user(db, current_user)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    user_claims = {
        'username': user.username,
        'is_admin': user.is_admin,
    }

    new_access_token = Authorize.create_access_token(
        subject=user.uid, user_claims=user_claims, fresh=False)

    Authorize.set_access_cookies(new_access_token)

    return {'msg': 'Refreshed successfully'}


@router.post('/sign-out')
async def sign_out(Authorize: Annotated[AuthJWT, Depends()]):
    Authorize.unset_jwt_cookies()

    return {'msg': 'Signed out successfully'}
