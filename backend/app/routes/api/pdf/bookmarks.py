from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models import HeaderConfig
from app.utils.pdf.bookmarks import create as create_bookmarked_pdf
from app.utils.pdf import get_file_path_from_id

router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks"],
)

TASKS = {}


class CreateBookmarkedPdfRequest(BaseModel):
    file_id: str
    header_config: HeaderConfig


@router.post("/create")
async def create_task_to_create_pdf_with_bookmarks(req: CreateBookmarkedPdfRequest):
    file_path = get_file_path_from_id(req.file_id)
    out_file_path = file_path.parent / f"{file_path.name}_bookmarked.pdf"

    TASKS[req.file_id] = create_bookmarked_pdf.delay(
        iput_pdf_path=file_path,
        out_pdf_path=out_file_path,
        header_config=req.header_config,
    )

    return {"message": "Task created successfully."}


@router.get("/status/{file_id}")
async def check_creation_status(file_id: str):
    if file_id not in TASKS:
        return {
            "message": "Task not found.",
            "error": True,
            "ready": None,
        }
    return {
        "message": "Task found.",
        "ready": TASKS[file_id].ready(),
        "error": False,
    }



@router.get("/get/{file_id}")
async def get_bookmarked_pdf(file_id: str):
    file_path = get_file_path_from_id(file_id)
    out_file_path = file_path.parent / f"{file_path.name}_bookmarked.pdf"

    return StreamingResponse(
        open(out_file_path, "rb"),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=bookmarked.pdf"},
    )
