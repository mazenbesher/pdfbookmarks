include ../.env

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate $(ENV_NAME)
UVICORN_CMD=$(CONDA_ACTIVATE); uvicorn app.__main__:app --port $(BACKEND_PORT) --host $(BACKEND_HOST) --reload

dev-tmux:
ifeq ($(TMUX),)
	@echo "Outside tmux"
	@echo "This command should be run inside tmux session"
else
	@echo "Inside tmux"
	@echo "Note: Order is important: first db!"

	@echo "Rename pane title to redis and run make dev in the current pane"
	tmux select-pane -t $(ENV_NAME):backend -T "redis"
	tmux send-keys -t $(ENV_NAME):backend "make start-redis-server" ENTER

	@echo "Split current horizontally"
	tmux split-window -t $(ENV_NAME):backend -h

	@echo "Rename the newly focused empty pane to uvicorn and run make start-uvicorn-dev"
	tmux select-pane -t $(ENV_NAME):backend -T "uvicorn"
	tmux send-keys -t $(ENV_NAME):backend "make start-uvicorn-dev" ENTER
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

start-redis-server:
	redis-server --port $(REDIS_PORT) --bind $(REDIS_HOST)
