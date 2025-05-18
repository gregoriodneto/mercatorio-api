from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.interfaces.routes.router import router

import app.scripts.create_table

app = FastAPI(
    title="Mercatorio Backend Challenge",
    version="1.0.0",
    description="API para cadastro de precatorios e credores",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return { "status": "ok", "msg": "Mercatório API Running!" }