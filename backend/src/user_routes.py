from fastapi import APIRouter, Depends
from .auth import get_current_user
from .models import User
from .database import SessionLocal
from sqlalchemy.future import select

router = APIRouter(prefix="/api/user", tags=["user"])

@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "username": current_user.username}

@router.get("/my_appointments")
async def get_my_appointments(current_user: User = Depends(get_current_user)):
    session = SessionLocal()
    result = await session.execute(select(current_user.__class__).where(current_user.__class__.id == current_user.id))
    user = result.scalar_one()
    await session.close()
    return [
        {
            "id": a.id,
            "master_id": a.master_id,
            "procedure_id": a.procedure_id,
            "datetime": a.datetime,
            "status": a.status
        }
        for a in user.appointments
    ]