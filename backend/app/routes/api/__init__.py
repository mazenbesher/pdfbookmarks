from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["api"],
)

from .pdf import router as pdf_router

router.include_router(pdf_router)
