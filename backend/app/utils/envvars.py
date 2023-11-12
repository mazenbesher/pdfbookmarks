from dotenv import dotenv_values

from app.definitions import ROOT_DIR

envvars = dotenv_values(ROOT_DIR / ".env")
