from pydantic import BaseModel


class HeaderConfig(BaseModel):
    bold: bool
    min_font_size: float
