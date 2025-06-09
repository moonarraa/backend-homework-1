from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class MasterCreate(BaseModel):
    name: str

class MasterRead(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class ProcedureCreate(BaseModel):
    name: str
    description: str

class ProcedureRead(BaseModel):
    id: int
    name: str
    description: str
    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    user_id: int
    master_id: int
    procedure_id: int
    datetime: datetime

class AppointmentRead(BaseModel):
    id: int
    user_id: int
    master_id: int
    procedure_id: int
    datetime: datetime
    status: str
    class Config:
        orm_mode = True 