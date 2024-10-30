from pydantic import BaseModel
from typing import List, Optional

# class KaliHost(Base):
#     __tablename__ = "kali_host"
    
#     id = Column(BigInteger, primary_key=True, index=True)
#     os = Column(String)
#     ip = Column(String)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     kali_host_service = relationship("KaliHostService", back_populates="kali_host")

# class KaliHostService(Base):
#     __tablename__ = "kali_host_service"

#     id = Column(BigInteger, primary_key=True, index=True)
#     kali_host_id = Column(BigInteger, ForeignKey("kali_host.id"))
#     service = Column(String)
#     port = Column(Integer)

#     kali_host = relationship("KaliHost", back_populates="kali_host_service")


# # KaliHostService에 대한 Vulnerability result
# class Vulnerability(Base):
#     __tablename__ = "vulnerability"

#     id = Column(BigInteger, primary_key=True, index=True)
#     kali_host_service_id = Column(BigInteger, ForeignKey("kali_host_service.id"))
#     name = Column(String)
#     cvss = Column(String, nullable=True)
#     title = Column(String)
#     description = Column(String)
#     url = Column(String)
#     type = Column(String)

class KaliHostBase(BaseModel):
    os : str
    ip : str
    uid : int

class KaliHostCreate(KaliHostBase):
    pass

class KaliHost(KaliHostBase):
    id : int


    class Config:
        orm_mode = True

class KaliHostUpdate(KaliHostBase): 
    pass

class KaliHostServiceBase(BaseModel):
    service : str
    port : int
    kali_host_id : int
    banner : Optional[str]

class KaliHostServiceCreate(KaliHostServiceBase):
    pass

class KaliHostService(KaliHostServiceBase):
    id : int

    class Config:
        orm_mode = True

class KaliHostServiceUpdate(KaliHostServiceBase):
    pass

class KaliProductBase(BaseModel):
    type : str
    name : str
    version : str
    vendor : str
    kali_host_service_id : int

class KaliProductCreate(KaliProductBase):
    pass

class KaliProduct(KaliProductBase):
    id : int

    class Config:
        orm_mode = True

class KaliProductUpdate(KaliProductBase):
    pass

class VulnerabilityBase(BaseModel):
    name : str
    cvss : str
    title : str
    description : str
    url : str
    type : str

class VulnerabilityCreate(VulnerabilityBase):
    pass

class Vulnerability(VulnerabilityBase):
    id : int
    kali_host_service_id : int

    class Config:
        orm_mode = True

class VulnerabilityUpdate(VulnerabilityBase):
    pass