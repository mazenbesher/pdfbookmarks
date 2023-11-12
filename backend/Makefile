include ../.env

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate $(ENV_NAME)
UVICORN_CMD=$(CONDA_ACTIVATE); uvicorn app.__main__:app --port $(BACKEND_PORT) --host $(BACKEND_HOST) --reload
CELERY_CMD=$(CONDA_ACTIVATE); celery -A app.celery worker

dev-tmux:
ifeq ($(TMUX),)
	@echo "Outside tmux"
	@echo "This command should be run inside tmux session"
else
	@echo "Inside tmux"
	@echo "Note: Order is important: first run redis than uvicorn!"

	@echo "Rename current window to redis and start redis server in the current window"
	tmux rename-window -t $(ENV_NAME) "redis"
	tmux send-keys -t $(ENV_NAME):redis "make start-redis-server-dev" ENTER

	@echo "Create new window, rename it to uvicorn and run make start-uvicorn-dev"
	tmux new-window -t $(ENV_NAME) -n "uvicorn"
	tmux send-keys -t $(ENV_NAME):uvicorn "make start-uvicorn-dev" ENTER
	
	@echo "Create new window, rename it to celery and run make start-celery-dev"
	tmux new-window -t $(ENV_NAME) -n "celery"
	tmux send-keys -t $(ENV_NAME):celery "make start-celery-dev" ENTER
endif


start-uvicorn-dev: clear-tmp
	$(UVICORN_CMD) --reload

start-uvicorn: clear-tmp
	$(UVICORN_CMD)

clear-tmp:
	rm -rf tmp/*

format:
	$(CONDA_ACTIVATE); ruff format .

open-docs:
	open http://$(BACKEND_HOST):$(BACKEND_PORT)/docs

start-redis-server-dev:
	redis-server --port $(REDIS_PORT) --bind $(REDIS_HOST)

start-redis-server: start-redis-server-dev

start-celery-dev:
	$(CELERY_CMD) --loglevel=INFO

start-celery:
	$(CELERY_CMD)
