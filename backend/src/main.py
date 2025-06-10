from fastapi import FastAPI
from .database import engine
from .models import Base
from fastapi.middleware.cors import CORSMiddleware
from .routers import routes
from .auth_routes import router as auth_router
from .user_routes import router as user_router   
from .routers import chatbot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chatbot.router)