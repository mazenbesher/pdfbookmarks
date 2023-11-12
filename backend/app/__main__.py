from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routes.api import router as api_router
from app.definitions import DIST_DIR
from app.lifespan import lifespan
from app.utils.envvars import envvars


# create FastAPI app
app = FastAPI(
    lifespan=lifespan,
)

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"http://{envvars['BACKEND_HOST']}:{envvars['BACKEND_PORT']}",
        f"http://{envvars['BACKEND_HOST']}:{envvars['VITE_PORT']}",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount routes
app.include_router(api_router)


app.mount(
    "/",
    StaticFiles(
        directory=DIST_DIR,
        html=True,
        check_dir=True,
    ),
    name="static",
)
