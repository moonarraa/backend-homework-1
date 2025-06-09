from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .database import SessionLocal
from .models import User
from .auth import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    session = SessionLocal()
    user = User(username=form_data.username, hashed_password=get_password_hash(form_data.password))
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
    except Exception:
        await session.rollback()
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        await session.close()
    return {"msg": "User created"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    session = SessionLocal()
    result = await session.execute(select(User).where(User.username == form_data.username))
    user = result.scalar_one_or_none()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    await session.close()
    return {"access_token": access_token, "token_type": "bearer"}

