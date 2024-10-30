from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey, ARRAY
from datetime import datetime

from sqlalchemy.orm import relationship
from model.database import Base

class TestRecord(Base):
    __tablename__ = "test_record"

    id = Column(BigInteger, primary_key=True, index=True)
    uid = Column(BigInteger)
    name = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

    cve_result = relationship("CVEResult", back_populates="test_record")