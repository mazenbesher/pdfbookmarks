from pydantic import BaseModel


class HeaderConfig(BaseModel):
    bold: bool
    min_font_size: float


class PreviewPageWithHeaderConfigRequest(BaseModel):
    file_id: str
    page_number: int
    header_config: HeaderConfig


class DownloadBookmarkedPdfRequest(BaseModel):
    file_id: str
    header_config: HeaderConfig
