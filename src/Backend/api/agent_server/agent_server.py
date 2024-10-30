from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse

import asyncio

import os

from model.database import SessionLocal

from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from fastapi_jwt_auth import AuthJWT

from model.database import get_db
from model.agent import schemas as agent_schemas
from model.agent import crud as agent_crud

from model.attack import schemas as attack_schemas
from model.attack import crud as attack_crud

from model.result import schemas as result_schemas
from model.result import crud as result_crud

from agent_server.parser import basic_parser

import base64

router = APIRouter(
    prefix='/agent_server',
    tags=['agent_server'],
    responses={404: {'description': 'Not Found'}},
)
    # host_dir_staged = Column(String, nullable=True)
    # host_file_path = Column(String, nullable=True)
    # host_dir_compress = Column(String, nullable=True)
    # host_file_name = Column(String, nullable=True)
    # wifi_network_ssid = Column(String, nullable=True)
    # host_user_name = Column(String, nullable=True)
    # domain_user_name = Column(String, nullable=True)

def update_host_info_key(save_to: str, output: str, db: Annotated[Session, Depends(get_db)], agent_id: int):
    if(save_to == 'host_dir_staged'):
        result_crud.update_host_dir_staged(db, agent_id, output)
    elif(save_to == 'host_file_path'):
        result_crud.update_host_file_path(db, agent_id, output)
    elif(save_to == 'host_dir_compress'):
        result_crud.update_host_dir_compress(db, agent_id, output)
    elif(save_to == 'host_file_name'):
        result_crud.update_host_file_name(db, agent_id, output)
    elif(save_to == 'wifi_network_ssid'):
        result_crud.update_wifi_network_ssid(db, agent_id, output)
    elif(save_to == 'host_user_name'):
        result_crud.update_host_user_name(db, agent_id, output)
    elif(save_to == 'domain_user_name'):
        result_crud.update_domain_user_name(db, agent_id, output)
    elif(save_to == 'remote_execution_smb'):
        result_crud.update_remote_execution_smb(db, agent_id, output)
    else:
        return {"message": "Error"}


@router.post('/connect/{uid}')
async def connect(uid: int, request: Request, db: Annotated[Session, Depends(get_db)]):
    data = await request.json()

    # Save received system information into the database
    # Example: Assuming `agent_schemas.AgentCreate` is a schema for agent data
    try:
        agent_check = agent_crud.get_agent_by_hostname_with_uid_and_os(db, data['hostname'], uid, data['os'])
        if agent_check:
            agent_data = agent_schemas.AgentUpdate(
                uid=uid,
                hostname=data['hostname'],
                ip=data['ip'],
                os=data['os'],
                connected=True,
                last_checkin=datetime.now()
            )
            agent_crud.update_agent(db, agent_check.id, agent_data)
        else:
            agent_data = agent_schemas.AgentCreate(
                uid=uid,
                hostname=data['hostname'],
                ip=data['ip'],
                os=data['os'],
                connected=True
            )
            agent_created = agent_crud.create_agent(db, agent_data)
            agent_crud.create_agent_prepare(db, agent_schemas.AgentPrepareCreate(agent_id=agent_created.id, commands=[], payloads=[], real_commands=[], status='finish'))

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "Connection established successfully"}

@router.post('/get_commands/{uid}')
async def get_commands(uid: int, request: Request, db: Annotated[Session, Depends(get_db)]):
    data = await request.json()

    try:
        agent_check = agent_crud.get_agent_by_hostname_with_uid_and_os(db, data['hostname'], uid, data['os'])
        if agent_check:
            agent_crud.update_agent_connected(db, agent_check.id, True)
            # Fetch commands from the database
            check_status = agent_crud.get_agent_prepare_status(db, agent_check.id)
            
            if check_status == 'prepare':
                print(1)
                commands = agent_crud.get_agent_prepare_commands(db, agent_check.id)
                print(f"Commands: {commands}")
                payloads = agent_crud.get_agent_prepare_payloads(db, agent_check.id)
                print(payloads)
                real_commands = agent_crud.get_agent_prepare_real_commands(db, agent_check.id)
                print(real_commands)

                if commands or payloads :                
                # Update status to proceed
                   agent_crud.update_agent_prepare_status_to_proceed(db, agent_check.id)
                print(f"Commands: {commands}")
                return {"commands": commands, "payloads": payloads, "real_commands": real_commands}
            else:
                return {"message": "connection check"}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))    

@router.post('/get_payloads/{payload}')
async def get_payloads(payload: str, db: Annotated[Session, Depends(get_db)]):
    try:
        print(f"Payload: {payload}")
        file_path = os.path.join(os.getcwd(), 'model', 'attack', 'payloads', payload)
        print(f"File path: {file_path}")
        if not os.path.isfile(file_path):
            raise HTTPException(status_code=404, detail="Payload not found")

        return FileResponse(file_path, media_type='application/octet-stream', filename=payload)

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/send_results/{uid}')
async def send_results(request: Request,  uid: int, db: Annotated[Session, Depends(get_db)]):
    # Save received command output into the database


    try:
        data = await request.json()
        print(f"Run Command : {data.get('command')}")

        print(f"Received command output: {data.get('output')}")
        agent_check = agent_crud.get_agent_by_hostname_with_uid_and_os(db, data['hostname'], uid, data['os'])
        if agent_check:
            output = data.get('output')
            if data.get('command').startswith("usernaem"):
                output = result_crud.get_host_user_name(db, agent_check.id)
            cmdresult_check = result_crud.get_command_result_by_command(db, agent_check.id, data.get('command'))
            check_success = basic_parser.windows_command(output)
            check_attack_id = attack_crud.get_attack_id_by_commnad(db, data.get('command'))
            if cmdresult_check:
                print(f"1")
                save_to = attack_crud.get_command_by_command(db, data.get('command')).save_to
                if save_to:
                    print(f"Save to: {save_to}")
                    for save in save_to:
                        check = result_crud.get_host_info(db, agent_check.id)
                        if check is None:
                            result_crud.create_host_info(db, result_schemas.HostInfoCre1ate(agent_id=agent_check.id, host_dir_staged="", host_file_path="", host_dir_compress="", host_file_name="", wifi_network_ssid="", host_user_name="", domain_user_name="", remote_execution_smb="")) 
                        update_host_info_key(save, output, db, agent_check.id)
                print(f"2")
                result_data = result_schemas.CommandResultUpdate(
                    agent_id=agent_check.id,
                    input_command=data.get('command'),
                    output_command=output,
                    success=check_success,
                    attack_id=check_attack_id
                )
                result_crud.update_command_result_output(db, cmdresult_check.id, result_data)
            else:
                save_to = attack_crud.get_command_by_command(db, data.get('command')).save_to
                if save_to:
                    print(f"3")
                    for save in save_to:
                        check = result_crud.get_host_info(db, agent_check.id)
                        if check is None:
                            result_crud.create_host_info(db, result_schemas.HostInfoCreate(agent_id=agent_check.id, host_dir_staged="", host_file_path="", host_dir_compress="", host_file_name="", wifi_network_ssid="", host_user_name="", domain_user_name="", remote_execution_smb="")) 
                        update_host_info_key(save, data.get('output'), db, agent_check.id)

                print(f"4")
                cmdresult = result_schemas.CommandResultCreate(
                    agent_id=agent_check.id,
                    input_command=data.get('command'),
                    output_command=output,
                    success=check_success,
                    attack_id=check_attack_id
                )
                result_crud.create_command_result(db, cmdresult)

        agent_crud.update_agent_prepare_status_to_finish(db, agent_check.id)
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Error"}

    # Update status to finish
    
    return {"message": "Success"}

async def disconnect_inactive_agents():
    while True:
        await asyncio.sleep(10)  # 주기적으로 실행 (10초 간격)
        # 데이터베이스 세션 직접 생성
        db: Session = SessionLocal()
        try:
            agents = agent_crud.get_all_agents_connected(db)
            for agent in agents:
                if agent.connected and (datetime.now() - agent.last_checkin > timedelta(seconds=15)):
                    agent_crud.update_agent_connected(db, agent.id, False)
                    agent_crud.update_agent_prepare_status_to_finish(db, agent.id)
                    print(f"Agent {agent.id} disconnected due to inactivity")
        except Exception as e:
            print(f"Error in disconnect_inactive_agents: {e}")
        finally:
            db.close()  # 세션을 사용한 후 반드시 닫아야 합니다.

# 서버 시작 시 비동기적으로 inactive 에이전트 검사 시작
@router.on_event("startup")
async def startup_event():
    asyncio.create_task(disconnect_inactive_agents())