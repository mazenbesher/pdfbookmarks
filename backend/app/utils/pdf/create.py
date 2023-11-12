import pdfplumber
import pdfplumber.page
import pypdf
from pypdf.generic import Fit

from app.models import HeaderConfig
from .headers import get_page_header_chars


def bookmarked(
    iput_pdf_path: str,
    out_pdf_path: str,
    header_config: HeaderConfig,
):
    pdfplumber_file = pdfplumber.open(iput_pdf_path)

    merger = pypdf.PdfMerger()
    merger.append(iput_pdf_path, import_outline=False)

    for page_num, pdf_page in enumerate(pdfplumber_file.pages):
        header_chars = get_page_header_chars(pdf_page, header_config)
        header_tops = set([char["y1"] for char in header_chars])
        header_chars_by_tops = {
            top: [char for char in header_chars if char["y1"] == top]
            for top in header_tops
        }
        header_lines_by_tops = {
            top: "".join([char["text"] for char in header_chars_by_tops[top]])
            for top in header_tops
        }

        # sort header_lines_by_tops by top value from highest to lowest
        header_lines_by_tops = dict(
            sorted(header_lines_by_tops.items(), key=lambda item: item[0], reverse=True)
        )

        for header_top, header_line in header_lines_by_tops.items():
            header_line = header_line.strip()
            if header_line == "":
                continue
            merger.add_outline_item(
                title=header_line,
                page_number=page_num,
                parent=None,
                color=(0.0, 0.0, 0.0),  # TODO: test
                bold=False,  # TODO: test
                italic=False,  # TODO: test
                fit=Fit.fit_horizontally(top=header_top),
            )

    merger.write(out_pdf_path)
    merger.close()
