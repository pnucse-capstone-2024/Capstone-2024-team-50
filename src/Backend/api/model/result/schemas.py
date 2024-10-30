from datetime import datetime
from pydantic import BaseModel

class CommandResultBase(BaseModel):
    agent_id: int
    input_command: str
    output_command: str
    success: bool
    attack_id: int

class CommandResultCreate(CommandResultBase):
    pass

class CommandResult(CommandResultBase):
    id: int

    class Config:
        orm_mode = True

class CommandResultUpdate(CommandResultBase):
    pass

class HostInfoBase(BaseModel):
    agent_id: int
    host_dir_staged: str
    host_file_path: str
    host_dir_compress: str
    host_file_name: str
    wifi_network_ssid: str
    host_user_name: str
    domain_user_name: str
    remote_execution_smb: str

class HostInfoCreate(HostInfoBase):
    pass

class HostInfo(HostInfoBase):
    id: int

    class Config:
        orm_mode = True

class HostInfoUpdate(HostInfoBase):
    pass