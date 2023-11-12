from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.utils import tmpdir
from app.utils import db


def startup():
    tmpdir.init()
    db.init()


def shutdown():
    tmpdir.cleanup()


@asynccontextmanager
async def lifespan(app: FastAPI):
    startup()
    yield
    shutdown()
