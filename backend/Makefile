include ../.env

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate $(ENV_NAME)
UVICORN_CMD=$(CONDA_ACTIVATE); uvicorn main:app --port $(BACKEND_PORT) --host $(BACKEND_URL) --reload

dev: clear-tmp
	$(UVICORN_CMD) --reload

start: clear-tmp
	$(UVICORN_CMD)

clear-tmp:
	rm -rf tmp/*

format:
	$(CONDA_ACTIVATE); ruff format .
