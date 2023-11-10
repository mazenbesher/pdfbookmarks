include .env

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate $(ENV_NAME)

dev:
	tmux new -d       -s $(ENV_NAME)
	tmux send-keys    -t $(ENV_NAME) "cd backend; make dev" ENTER
	tmux split-window -t $(ENV_NAME) -h
	tmux send-keys    -t $(ENV_NAME) "cd frontend; make dev" ENTER
	tmux a            -t $(ENV_NAME)

setup: setup-backend setup-frontend

setup-backend:
	mkdir backend
	@echo "Create Python env"
	conda create -n $(ENV_NAME) python=3.11 -y
	@echo "Install dependencies"
	$(CONDA_ACTIVATE); pip install "pdfplumber==0.10.3"
	$(CONDA_ACTIVATE); pip install "pypdf==3.17.0"
	$(CONDA_ACTIVATE); pip install "fastapi==0.104.1"
	$(CONDA_ACTIVATE); pip install "uvicorn[standard]==0.24.0"
	$(CONDA_ACTIVATE); pip install "python-multipart==0.0.6"
	$(CONDA_ACTIVATE); pip install "ruff==0.1.4"
	$(CONDA_ACTIVATE); pip install "python-dotenv==1.0.0"

setup-frontend: frontend
	cd frontend; bun install

frontend:
	@echo "Selected options:"
	@echo "1. Framework: Svelte"
	@echo "2. Variant: TypeScript"
	@echo "3. Additional options: None"
	bun create vite frontend
