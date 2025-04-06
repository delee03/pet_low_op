from fastapi import FastAPI
from app.routers import owner_router

app = FastAPI()

#Map routing
app.include_router(owner_router.router, prefix="/owners", tags=["owners"])