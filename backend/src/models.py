from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    appointments = relationship("Appointment", back_populates="user")

class Master(Base):
    __tablename__ = "masters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    appointments = relationship("Appointment", back_populates="master")

class Procedure(Base):
    __tablename__ = "procedures"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    appointments = relationship("Appointment", back_populates="procedure")

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    master_id = Column(Integer, ForeignKey("masters.id"))
    procedure_id = Column(Integer, ForeignKey("procedures.id"))
    datetime = Column(DateTime)
    status = Column(String, default="active")

    user = relationship("User", back_populates="appointments")
    master = relationship("Master", back_populates="appointments")
    procedure = relationship("Procedure", back_populates="appointments") 