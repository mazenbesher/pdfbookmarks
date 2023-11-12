import os

from pydantic import BaseModel
import pdfplumber

from app.types import T_PathLike


class PDFFileStatus(BaseModel):
    filename: str
    n_pages: int
    size: int
    last_accessed: float
    last_modified: float
    creation_time: float


def get_file_status(filename: str, pdf_file_path: T_PathLike):
    file_stat = os.stat(pdf_file_path)
    pdf_file = pdfplumber.open(pdf_file_path)
    return PDFFileStatus(
        filename=filename,
        n_pages=len(pdf_file.pages),
        size=file_stat.st_size,
        last_accessed=file_stat.st_atime,
        last_modified=file_stat.st_mtime,
        creation_time=file_stat.st_ctime,
    )
