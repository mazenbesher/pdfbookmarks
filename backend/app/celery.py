from celery import Celery

from app.utils.envvars import envvars


celery_app = Celery(
    envvars["ENV_NAME"],
    broker=f"redis://{envvars['REDIS_HOST']}:{envvars['REDIS_PORT']}",
    backend=f"redis://{envvars['REDIS_HOST']}:{envvars['REDIS_PORT']}",
    # register tasks
    include=["app.utils.pdf.bookmarks"],
)

# configure celery
celery_app.conf.update(
    # to make celery work with pydantic models
    # https://stackoverflow.com/a/66854700/1617883
    task_serializer="pickle",
    result_serializer="pickle",
    event_serializer="json",
    accept_content=["application/json", "application/x-python-serialize"],
    result_accept_content=["application/json", "application/x-python-serialize"],
)
