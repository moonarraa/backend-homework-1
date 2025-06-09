from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from .models import User, Master, Procedure, Appointment
from passlib.hash import bcrypt
from datetime import datetime

# --- User CRUD ---
async def create_user(session: AsyncSession, username: str, password: str):
    hashed_password = bcrypt.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
    except Exception:
        await session.rollback()
        raise HTTPException(status_code=400, detail="Username already exists")
    return user

async def authenticate_user(session: AsyncSession, username: str, password: str):
    result = await session.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()
    if user and bcrypt.verify(password, user.hashed_password):
        return user
    raise HTTPException(status_code=401, detail="Invalid credentials")

# --- Master CRUD ---
async def create_master(session: AsyncSession, name: str):
    master = Master(name=name)
    session.add(master)
    await session.commit()
    await session.refresh(master)
    return master

async def read_masters(session: AsyncSession):
    result = await session.execute(select(Master))
    return result.scalars().all()

# --- Procedure CRUD ---
async def create_procedure(session: AsyncSession, name: str, description: str):
    procedure = Procedure(name=name, description=description)
    session.add(procedure)
    await session.commit()
    await session.refresh(procedure)
    return procedure

async def read_procedures(session: AsyncSession):
    result = await session.execute(select(Procedure))
    return result.scalars().all()

# --- Appointment CRUD ---
async def create_appointment(session: AsyncSession, user_id: int, master_id: int, procedure_id: int, dt: datetime):
    appointment = Appointment(user_id=user_id, master_id=master_id, procedure_id=procedure_id, datetime=dt)
    session.add(appointment)
    await session.commit()
    await session.refresh(appointment)
    return appointment

async def read_appointments_for_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(Appointment).where(Appointment.user_id == user_id))
    return result.scalars().all() 