include .env

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate $(ENV_NAME)

dev-tmux:	
	@echo "Create tmux session with name $(ENV_NAME)"
	tmux new -d -s $(ENV_NAME)

	@echo "Enable pane titles in tmux"
	tmux set -t $(ENV_NAME) pane-border-status top
	
	@echo "Creat a new window with name backend and run 'cd backend; make dev-tmux' in it"
	tmux rename-window -t $(ENV_NAME) "backend"
	tmux select-pane -t $(ENV_NAME):backend -T "backend"
	tmux send-keys -t $(ENV_NAME):backend "cd backend; make dev-tmux" ENTER
	
	@echo "Creat a new window with name frontend and run 'cd frontend; make dev-tmux' in it"
	tmux new-window -t $(ENV_NAME) -n "frontend"
	tmux select-pane -t $(ENV_NAME):frontend -T "frontend"
	tmux send-keys -t $(ENV_NAME):frontend "cd frontend; make dev-tmux" ENTER
	
	tmux a -t $(ENV_NAME)

setup: setup-backend setup-frontend

setup-backend:
	@echo "Create conda env"
	conda create -n $(ENV_NAME) python=3.11 -y

	@echo "Install pytohn dependencies"
	$(CONDA_ACTIVATE); pip install "pdfplumber==0.10.3"
	$(CONDA_ACTIVATE); pip install "pypdf==3.17.0"
	$(CONDA_ACTIVATE); pip install "fastapi==0.104.1"
	$(CONDA_ACTIVATE); pip install "uvicorn[standard]==0.24.0"
	$(CONDA_ACTIVATE); pip install "python-multipart==0.0.6"
	$(CONDA_ACTIVATE); pip install "ruff==0.1.4"
	$(CONDA_ACTIVATE); pip install "python-dotenv==1.0.0"
	$(CONDA_ACTIVATE); pip install "redis==5.0.1"

	@echo "Install other dependencies"
	brew install redis@7.2

setup-frontend: frontend
	cd frontend; bun install

frontend:
	@echo "Selected options:"
	@echo "1. Framework: Svelte"
	@echo "2. Variant: TypeScript"
	@echo "3. Additional options: None"
	bun create vite frontend
