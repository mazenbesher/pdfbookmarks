import io

from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import pdfplumber
from pdfplumber.display import PageImage

from app.models import HeaderConfig
from app.utils.pdf import get_file_path_from_id
import app.utils.pdf.headers

router = APIRouter(
    prefix="/page",
    tags=["page"],
)


class PreviewPageWithHeaderConfigRequest(BaseModel):
    file_id: str
    page_number: int
    header_config: HeaderConfig


@router.post(
    "/preview",
    # responses={200: {"content": {"image/png": {}}}},
)
async def preview(req: PreviewPageWithHeaderConfigRequest):
    # open requested page
    single_page_pdf_file = pdfplumber.open(
        get_file_path_from_id(req.file_id),
        pages=[req.page_number],
    )

    # get page image with headers
    page_image: PageImage = app.utils.pdf.headers.to_page_image_with_headers(
        pdf_file=single_page_pdf_file,
        header_config=req.header_config,
    )

    # save to buffer as PNG image
    img_buf = io.BytesIO()
    page_image.save(img_buf, format="PNG")
    img_buf.seek(0)

    # return image
    return StreamingResponse(content=img_buf, media_type="image/png")
