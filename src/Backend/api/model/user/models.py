from datetime import datetime

from sqlalchemy import Column, BigInteger,  String, Boolean, DateTime
from sqlalchemy.orm import relationship

from model.database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(BigInteger, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, default=None)
