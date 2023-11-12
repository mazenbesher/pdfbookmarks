import pdfplumber
from app.models import HeaderConfig


def get_page_header_chars(
    pdf_page: pdfplumber.page.Page,
    header_config: HeaderConfig,
):
    fonts = set([char["fontname"] for char in pdf_page.chars])
    bold_fonts = set([font for font in fonts if "bold" in font.lower()])
    header_chars = [
        char
        for char in pdf_page.chars
        if (header_config.bold and char["fontname"] in bold_fonts)
        and (header_config.min_font_size and char["size"] > header_config.min_font_size)
    ]
    return header_chars


def to_page_image_with_headers(
    pdf_file: pdfplumber.PDF,
    header_config: HeaderConfig,
    page_num: int = 0,
):
    """
    Extracts header based on the config and shows it on the page
    """
    page = pdf_file.pages[page_num]
    header_chars = get_page_header_chars(page, header_config)
    img = page.to_image()
    img = img.draw_rects(header_chars)
    return img
