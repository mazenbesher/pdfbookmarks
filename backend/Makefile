include ../.env

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate pdfbookmarks

dev: clear-tmp
	$(CONDA_ACTIVATE); uvicorn main:app --port $(BACKEND_PORT) --reload

start:
	$(CONDA_ACTIVATE); uvicorn main:app --port $(BACKEND_PORT)

clear-tmp:
	rm -rf tmp/*

format:
	$(CONDA_ACTIVATE); ruff format .
