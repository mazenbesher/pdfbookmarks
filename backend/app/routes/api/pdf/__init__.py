import uuid

from fastapi import APIRouter
from fastapi import UploadFile

import app.utils.pdf.status
from app.utils.pdf import get_file_path_from_id
from app.utils import db

from .page import router as page_router
from .download import router as download_router

router = APIRouter(
    prefix="/pdf",
    tags=["pdf"],
)
router.include_router(page_router)
router.include_router(download_router)


@router.post("/upload")
async def upload_file(file: UploadFile):
    # generate random uuid for file
    file_id = str(uuid.uuid4())
    file_path = get_file_path_from_id(file_id)

    # save file to temporary directory
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # save file status to db
    db.get_conn().hset(
        file_id,
        mapping=dict(
            app.utils.pdf.status.get_file_status(
                filename=file.filename,
                pdf_file_path=file_path,
            ),
        ),
    )

    # return file id
    return {"file_id": file_id}


@router.get("/status/{file_id}")
async def get_file_status(file_id: str):
    # check fileid exists in db
    if not db.get_conn().exists(file_id):
        return {"error": "File ID does not exist."}

    filestatus: dict = db.get_conn().hgetall(file_id)
    filestatus = app.utils.pdf.status.PDFFileStatus.model_validate(filestatus)
    return filestatus
