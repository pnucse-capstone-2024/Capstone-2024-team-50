from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

import string

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.result import schemas as result_schemas
from model.result import crud as result_crud

from model.agent import schemas as agent_schemas
from model.agent import crud as agent_crud

router = APIRouter(
    prefix='/result',
    tags=['result'],
    responses={404: {'description': 'Not Found'}},
)

@router.post('/all_commands/{uid}')
async def get_all_commands(uid: int, db: Annotated[Session, Depends(get_db)]):
    try:
        agents = agent_crud.get_agents(db, uid)
        if not agents:
            raise Exception('No agents found')
        agents_id = [agent.id for agent in agents]        

        # id : [], id : []
        commands = {}
        for agent_id in agents_id:
            command_results = result_crud.get_command_results(db, agent_id)
            if command_results:
                commands[agent_id] = [command_result for command_result in command_results]

        return commands

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post('/check_success/{uid}/{tid}')
async def check_success(uid: int, tid: str, db: Annotated[Session, Depends(get_db)]):
    try:
        command_results = result_crud.get_command_results_by_tid(db, tid, uid)
        if not command_results:
            raise Exception('No command results found')
        
        for command_result in command_results:
            if command_result.success:
                return True
        
        return False

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post('/get_success_scenarios/{aid}')
async def get_success_scenario(aid: int, db: Annotated[Session, Depends(get_db)]):
    try:
        success_attacks = result_crud.get_scenario_success_by_aid(db, aid)
        if not success_attacks:
            return {"message": "No success attacks found"}
        
        return success_attacks

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))