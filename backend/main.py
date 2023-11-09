import os
import io
import uuid

import pdfplumber
from pdfplumber.display import PageImage
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

import pdf
import models

# load environment variables from .env file
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"http://localhost:{os.environ.get('VITE_SERVER_PORT')}",
        f"http://localhost:{os.environ.get('BACKEND_PORT')}",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/pdf/upload")
async def upload_file(file: UploadFile):
    # generate random uuid for file
    file_id = str(uuid.uuid4())

    # save file to temporary directory
    with open(f"tmp/{file_id}.pdf", "wb") as buffer:
        buffer.write(await file.read())

    # return file id
    return {"file_id": file_id}


@app.post(
    "/api/pdf/preview/headers",
    responses={200: {"content": {"image/png": {}}}},
)
async def prview_page(req: models.PreviewPageWithHeaderConfigRequest):
    print(req)
    single_page_pdf_file = pdfplumber.open(
        f"tmp/{req.file_id}.pdf",
        pages=[req.page_number],
    )
    page_image: PageImage = pdf.show_headers(
        pdf_file=single_page_pdf_file,
        header_config=req.header_config,
    )

    # save to buffer as PNG image
    img_buf = io.BytesIO()
    page_image.save(img_buf, format="PNG")
    img_buf.seek(0)
    return StreamingResponse(content=img_buf, media_type="image/png")


@app.post("/api/pdf/download/bookmarked")
async def download_bookmarked_pdf(req: models.DownloadBookmarkedPdfRequest):
    pdf.get_bookmarked_pdf(
        iput_pdf_path=f"tmp/{req.file_id}.pdf",
        out_pdf_path=f"tmp/{req.file_id}_bookmarked.pdf",
        header_config=req.header_config,
    )
    return StreamingResponse(
        open(f"tmp/{req.file_id}_bookmarked.pdf", "rb"),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=bookmarked.pdf"},
    )


app.mount(
    "/",
    StaticFiles(
        directory="../frontend/dist",
        html=True,
        check_dir=True,
    ),
    name="static",
)
