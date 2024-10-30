from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

import string
import re
import json

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.attack import schemas as attack_schemas
from model.attack import crud as attack_crud

from model.user import crud as user_crud
from model.user import schemas as user_schemas

from model.agent import schemas as agent_schemas
from model.agent import crud as agent_crud

from model.result import schemas as result_schemas
from model.result import crud as result_crud

router = APIRouter(
    prefix='/attack',
    tags=['attack'],
    responses={404: {'description': 'Not Found'}},
)

# // technique.tid가 tid
# // attack에 tid가 있음
# 같은 tid를 가진 attack은 여러개가 있을 수 있음
# // command에 attack_id와 platform가 있음
# // 그러면 사용자느 tid랑 uid를 보내주면 돼
# // 백엔드에서는 tid로 attack_id를 찾아서 platform을 찾아서 command를 실행시키면 됨
# 여기서, TMP에 해당 uid와 command를 넣어주면 돼 그럼 공격은 알아서 진행돼

def check_windows_linux_macos(os: str):
    # os를 소문자로 변형한 것 중에 Windows가 포함 된다면
    if 'windows' in os.lower():
        return ['windows', 'psh']
    if 'linux' in os.lower():
        return ['linux', 'sh']
    if 'mac' in os.lower():
        return ['darwin', 'sh']
    
@router.post('/{uid}/{tid}/{aid}')
async def real_attack(uid: int, tid: str, aid: int, db: Annotated[Session, Depends(get_db)]):
    try:
        attacks = attack_crud.get_attacks_by_tid(db, tid)
        agent = agent_crud.get_agent(db, aid)
        check_agent_prepare_status = agent_crud.get_agent_prepare_status(db, aid)
        if check_agent_prepare_status == 'proceed':
            print("뭐야이거")
            return {"message": ""}
        real_commands = []
        commands = []
        payloads = []
        if attacks:
            for attack in attacks:
                platform, shell_type = check_windows_linux_macos(agent.os)
                command = attack_crud.get_command_by_attack_id_and_platform_and_shell_type(db, attack.id, platform, shell_type)
                # print(command.command)
                if command:
                    replace_command = command.command
                    if "#{host.dir.staged}" in replace_command:
                        print("require host.dir.staged")
                        replace_word = result_crud.get_host_dir_staged(db, aid)
                        if replace_word is None:
                            replace_word = ""
                        replace_command = replace_command.replace("#{host.dir.staged}", replace_word)
                    if "#{host.file.path}" in replace_command:
                        print("require host.file.path")
                        replace_word = result_crud.get_host_file_path(db, aid)
                        if replace_word is None:
                            replace_word = ""
                        print("host.file.path: ", replace_word)
                        replace_command = replace_command.replace("#{host.file.path}", replace_word)
                    if "#{host.dir.compress}" in replace_command:
                        print("require host.dir.compress")
                        replace_word = result_crud.get_host_dir_compress(db, aid)
                        if replace_word is None:
                            replace_word = ""
                        print("host.dir.compress: ", replace_word)
                        replace_command = replace_command.replace("#{host.dir.compress}", replace_word)
                    if "#{host.user.name}" in replace_command:
                        print("require host.user.name")
                        replace_word = result_crud.get_host_user_name(db, aid)
                        if replace_word is None:
                            replace_word = ""
                        print("host.user.name: ", replace_word)
                        replace_command = replace_command.replace("#{host.user.name}", replace_word)
                    if "#{remote_host_ip}" in replace_command:
                        print("require remote_host_ip")
                        replace_word = agent.ip
                        print("remote_host_ip: ", replace_word)
                        replace_command = replace_command.replace("#{remote_host_ip}", replace_word)
                    if "#{host_user_name}" in replace_command:
                        print("require host_user_name")
                        replace_word = result_crud.get_host_user_name(db, aid)
                        if replace_word is None:
                            replace_word = ""
                        print("host_user_name: ", replace_word)
                        replace_command = replace_command.replace("#{host_user_name}", replace_word)
                    commands.append(command.command)
                    real_commands.append(replace_command)
                
                    payload = attack_crud.get_payload_by_command_id(db, command.id)
                    # print(payload.filename)
                    if payload:
                        payloads.append(payload.filename)

            agent_crud.update_agent_prepare_commands_and_payloads(db, aid, real_commands, commands, payloads)
            agent_crud.update_agent_prepare_status_to_prepare(db, aid)

            print("payload: ",payloads)
            print("commands: ",commands)
            print("real_commands: ",real_commands)
            return {"commands": command}
        else:
            raise HTTPException(status_code=404, detail="Attack not found")
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/test/linux/{uid}')
async def test_attack(uid: int, db: Annotated[Session, Depends(get_db)]):
    user_crud.test_linux(db, uid)

    return {"message": "Connection established successfully"}

@router.get('/test/{uid}')
async def test_attack( uid: int, db: Annotated[Session, Depends(get_db)]):
    tmp = user_crud.get_linux(db, uid)
    if tmp is None:
        raise HTTPException(status_code=404, detail="Attack not found")
    return {"message": tmp}
