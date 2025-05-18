from fastapi import APIRouter
from app.interfaces.controllers import credor_controller

router = APIRouter()

router.include_router(credor_controller.router)