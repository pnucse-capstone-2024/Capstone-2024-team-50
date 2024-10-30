from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

import re
import subprocess

from fastapi_jwt_auth import AuthJWT

from model.database import get_db

from model.kali_result import crud as kali_result_crud
from model.kali_result import schemas as kali_result_schemas

router = APIRouter(
    prefix="/kali_result",
    tags=['Kali_result'],
    responses={404: {"description": "Not found"}},
)

@router.post("/kali_hosts")
async def create_kali_host(db: Annotated[Session, Depends(get_db)], Authorize: Annotated[AuthJWT, Depends()]):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    
    kali_hosts = kali_result_crud.get_kali_hosts_by_uid(db, current_user)
    kali_host_services = kali_result_crud.get_kali_host_services_by_uid(db, current_user)

    if not kali_hosts:
        raise HTTPException(status_code=404, detail="Not Found")
    
    if not kali_host_services:
        raise HTTPException(status_code=404, detail="Not Found")

    result = []

    for host in kali_hosts:
        services = []
        tmp = {}
        for service in kali_host_services:
            if host.id == service.kali_host_id:
                vulnerabilities = kali_result_crud.get_vulnerabilities_by_kali_host_service_id(db, service.id)
                tmp_service = {
                    "id": service.id,
                    "port": service.port,
                    "service": service.service,
                    "vulnerabilities": vulnerabilities
                }          
                services.append(tmp_service) 
                tmp = {
                    "id": host.id,
                    "ip": host.ip,
                    "os": host.os,
                    "services": services
                }
                # print(tmp)
        if tmp == {}:
            continue
        result.append(tmp)

    print(result)
    return result

@router.post("/kali_host_services")
async def create_kali_host_services(db: Annotated[Session, Depends(get_db)], Authorize: Annotated[AuthJWT, Depends()]):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    result = kali_result_crud.get_kali_host_services_by_uid(db, current_user)

    if not result:
        raise HTTPException(status_code=404, detail="Not Found")
    
    return result