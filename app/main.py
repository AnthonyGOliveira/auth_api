from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ast
from app.controller.user_controller import router as authentication_router
from app.infrastructure.database_engine import Base, engine
from app.infrastructure.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ast.literal_eval(settings.ORIGINS)
methods = ast.literal_eval(settings.METHODS)
headers = ast.literal_eval(settings.HEADERS)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=settings.CREDENTIALS,
    allow_methods=methods,
    allow_headers=headers,
)

app.include_router(router=authentication_router, prefix='/api/authentication/user')


@app.get("/healthchecker")
def root():
    return {"message": "The API is LIVE!!"}