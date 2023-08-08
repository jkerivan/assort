from fastapi import APIRouter
from .endpoints import patients, call

router = APIRouter()

router.include_router(patients.router, prefix="/patients", tags=["patients"])
router.include_router(call.router, prefix="/calls", tags=["calls"])