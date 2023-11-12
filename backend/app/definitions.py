from pathlib import Path

curr_file_path = Path(__file__).resolve()

APP_DIR = curr_file_path.parent
BACKEDN_DIR = APP_DIR.parent
ROOT_DIR = BACKEDN_DIR.parent
FRONTEND_DIR = ROOT_DIR / "frontend"
DIST_DIR = FRONTEND_DIR / "dist"
