import tempfile
from typing import Optional
from pathlib import Path

_TMP_DIR: Optional[tempfile.TemporaryDirectory] = None


def init():
    global _TMP_DIR
    _TMP_DIR = tempfile.TemporaryDirectory()


def get():
    return _TMP_DIR


def cleanup():
    global _TMP_DIR
    _TMP_DIR.cleanup()
    _TMP_DIR = None


def get_path() -> Path:
    return Path(_TMP_DIR.name)
