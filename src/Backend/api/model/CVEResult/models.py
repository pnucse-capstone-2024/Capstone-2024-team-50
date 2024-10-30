from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from model.database import Base

class CVEResult(Base):
    __tablename__ = "cve_result"

    id = Column(BigInteger, primary_key=True, index=True)
    rid = Column(BigInteger, ForeignKey('test_record.id'))
    cid = Column(BigInteger, ForeignKey('cve_attacks.id'))
    is_success = Column(Boolean)

    test_record = relationship("TestRecord", back_populates="cve_result")
    cve_attacks = relationship("CVEAttacks", back_populates="cve_result")