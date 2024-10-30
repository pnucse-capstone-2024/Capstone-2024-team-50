from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, ARRAY, JSON
from sqlalchemy.orm import relationship
from model.database import Base

class KaliHost(Base):
    __tablename__ = "kali_host"
    
    id = Column(BigInteger, primary_key=True, index=True)
    uid = Column(BigInteger, ForeignKey("users.uid"))
    os = Column(String, nullable=True)
    ip = Column(String)

class KaliHostService(Base):
    __tablename__ = "kali_host_service"

    id = Column(BigInteger, primary_key=True, index=True)
    kali_host_id = Column(BigInteger, ForeignKey("kali_host.id"))
    service = Column(String)
    banner = Column(String, nullable=True)
    port = Column(Integer)

class KaliProduct(Base):
    __tablename__ = "kali_product"

    id = Column(BigInteger, primary_key=True, index=True)
    type = Column(String)
    name = Column(String)
    version = Column(String)
    vendor = Column(String)
    kali_host_service_id = Column(BigInteger, ForeignKey("kali_host_service.id"))

# KaliHostService에 대한 Vulnerability result
class Vulnerability(Base):
    __tablename__ = "vulnerability"

    id = Column(BigInteger, primary_key=True, index=True)
    kali_host_service_id = Column(BigInteger, ForeignKey("kali_host_service.id"))
    name = Column(String)
    cvss = Column(String, nullable=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    type = Column(String)