from fastapi import FastAPI
from app.controller.user_controller import router as authentication_router

app = FastAPI()

app.include_router(router=authentication_router, prefix='/authentication')