from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from model.database import Base

class Tactics(Base):
    __tablename__ = "tactics"

    id = Column(BigInteger, primary_key=True, index=True)
    taid = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String)

    techniques = relationship("Techniques", back_populates="tactics")

class Techniques(Base):
    __tablename__ = "techniques"

    id = Column(BigInteger, primary_key=True, index=True)
    tid = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    taid = Column(String, ForeignKey("tactics.taid"))

    tactics = relationship("Tactics", back_populates="techniques")
    attacks = relationship("Attacks", back_populates="techniques")
    # cve_attacks = relationship("CVEAttacks", back_populates="techniques")

class Commands(Base):
    __tablename__ = "commands"

    id = Column(BigInteger, primary_key=True, index=True)
    platform = Column(String)
    shell_type = Column(String)
    command = Column(String)
    cleanup = Column(String)
    attack_id = Column(BigInteger, ForeignKey("attacks.id"))
    save_to = Column(ARRAY(String))
    requirements = Column(ARRAY(String))

    payloads = relationship("Payloads", back_populates="commands")
    attacks = relationship("Attacks", back_populates="commands")

class Payloads(Base):
    __tablename__ = "payloads"

    id = Column(BigInteger, primary_key=True, index=True)
    filename = Column(String)
    command_id = Column(BigInteger, ForeignKey("commands.id"))

    commands = relationship("Commands", back_populates="payloads")

class Attacks(Base):
    __tablename__ = "attacks"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    tid = Column(String, ForeignKey("techniques.tid"))

    techniques = relationship("Techniques", back_populates="attacks")
    commands = relationship("Commands", back_populates="attacks")


# class Scenario(Base):
#     __tablename__ = "scenarios"

#     id = Column(BigInteger, primary_key=True, index=True)
#     name = Column(String)
#     description = Column(String)
#     attacks_ids = Column(ARRAY(BigInteger), ForeignKey("attacks.id"))

#     attacks = relationship("Attacks", back_populates="scenarios")

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    attack_names = Column(ARRAY(String))

### cve attack
class CVEAttacks(Base):
    __tablename__ = "cve_attacks"

    id = Column(BigInteger, primary_key=True, index=True)
    cve_id = Column(String)
    cve_platform = Column(String)
    cve_command = Column(String)
    cve_title = Column(String)
    cve_description = Column(String)
    cve_tid = Column(ARRAY(String))
    cve_mitigation = Column(String)

    cve_result = relationship("CVEResult", back_populates="cve_attacks")