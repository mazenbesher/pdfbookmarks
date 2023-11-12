from pathlib import Path

from app.utils import tmpdir


def get_file_path_from_id(file_id: str) -> Path:
    return tmpdir.get_path() / f"{file_id}.pdf"
