from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models import HeaderConfig
from app.utils.pdf.create import bookmarked
from app.utils.pdf import get_file_path_from_id

router = APIRouter(
    prefix="/download",
)


class DownloadBookmarkedPdfRequest(BaseModel):
    file_id: str
    header_config: HeaderConfig


@router.post("/bookmarked")
async def download_bookmarked_pdf(req: DownloadBookmarkedPdfRequest):
    file_path = get_file_path_from_id(req.file_id)
    out_file_path = file_path.parent / f"{file_path.name}_bookmarked.pdf"

    bookmarked(
        iput_pdf_path=file_path,
        out_pdf_path=out_file_path,
        header_config=req.header_config,
    )
    return StreamingResponse(
        open(out_file_path, "rb"),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=bookmarked.pdf"},
    )
