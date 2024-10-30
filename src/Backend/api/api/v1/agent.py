from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.agent import schemas as agent_schemas
from model.agent import crud as agent_crud

from api.v1 import connect_command

router = APIRouter(
    prefix='/agent',
    tags=['agent'],
    responses={404: {'description': 'Not Found'}},
)

@router.post('/all/{uid}', response_model=List[agent_schemas.Agent])
async def get_all_agents(uid:int, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]) :
    Authorize.jwt_required()

    agents = agent_crud.get_agents(db, uid)
    if not agents:
        return []

    return agents

@router.post('/connected/all/{uid}', response_model=List[agent_schemas.Agent])
async def get_all_agents_connected(uid:int, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]) :
    Authorize.jwt_required()

    agents = agent_crud.get_all_agents_connected(db)
    if not agents:
        return []

    return agents

@router.post('/command/{uid}')
async def create_agent(uid:int, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]) :
    Authorize.jwt_required()

    windows_command = connect_command.windows_command(uid)
    linux_command = connect_command.linux_command(uid)
    mac_command = connect_command.mac_command(uid)

    return {"windows": windows_command, "linux": linux_command, "mac": mac_command}

@router.delete('/delete/{aid}')
async def delete_agent(aid: int, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]) :
    Authorize.jwt_required()

    agent = agent_crud.delete_agent(db, aid)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    return {"message": "Agent deleted successfully"}

@router.post('/count/{uit}')
async def count_agents(uit:int, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]) :
    Authorize.jwt_required()

    count = agent_crud.count_agents(db, uit)
    return {"count": count}

@router.post('/prepare/status/{aid}')
async def get_agent_prepare_status(aid:int, Authorize: Annotated[AuthJWT, Depends()], db: Annotated[Session, Depends(get_db)]) :
    Authorize.jwt_required()

    agent_prepare_status = agent_crud.get_agent_prepare_status(db, aid)
    if not agent_prepare_status:
        return {"status": "not found"}
    
    return {"status": agent_prepare_status}