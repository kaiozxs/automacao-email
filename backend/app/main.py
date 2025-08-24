from fastapi import FastAPI
from app.routes import emails

app = FastAPI(title="Email Classifier API")

app.include_router(emails.router)