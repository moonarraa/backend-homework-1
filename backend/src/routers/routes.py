from fastapi import APIRouter, Depends, HTTPException
from ..services.parse_salons import fetch_salons
from fastapi import Query

router = APIRouter(prefix="/api/salons", tags=["salons"])


@router.get("/hair")
async def get_hair_salons(
    skip: int = 0,
    limit: int = 10,
    q: str = Query(None, description="Поиск салонов по названию")
):
    salons = await fetch_salons()
    if q:
        salons = [salon for salon in salons if q.lower() in salon["name"].lower()]
    return salons[skip:skip+limit]


@router.get("/hair/by-name/{name}")
async def get_salon_by_name(name: str):
    salons = await fetch_salons()
    for salon in salons:
        if salon["name"].lower() == name.lower():
            return salon
    raise HTTPException(status_code=404, detail="Salon not found")