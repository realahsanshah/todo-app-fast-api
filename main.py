from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.todos import todo

description_text = """
FastAPI TODO API Demo
"""
app = FastAPI(
    title="FastAPI TODO API Demo",
     description=description_text,
    version=settings.API_VERSION,
    contact=settings.CONTACT,
    terms_of_service="https://www.ktechhub.com/terms/",
)

app.include_router(todo.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)