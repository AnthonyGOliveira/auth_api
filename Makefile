# Variáveis
VENV_DIR=venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip
UVICORN=$(VENV_DIR)/bin/uvicorn
ALEMBIC=$(VENV_DIR)/bin/alembic
PYTEST=$(VENV_DIR)/bin/pytest
COVOPTS=--cov=app --cov-config=.coveragerc --cov-report=html --cov-report=term

# Criar o ambiente virtual
.PHONY: venv
venv:
	python -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip

# Instalar dependências
.PHONY: install
install: venv
	$(PIP) install -r requirements.txt

# Instalar dependências de desenvolvimento
.PHONY: install-dev
install-dev: install
	$(PIP) install -r requirements-dev.txt

# Executar a aplicação
.PHONY: run
run:
	$(UVICORN) app.main:app --reload

# Executar migrações do banco de dados
.PHONY: migrate
migrate:
	$(ALEMBIC) upgrade head

# Criar uma nova migração do banco de dados
.PHONY: makemigrations
makemigrations:
	$(ALEMBIC) revision --autogenerate -m "Nova migração"

# Limpar relatórios de cobertura antigos
.PHONY: clean-cov
clean-cov:
	rm -rf htmlcov

# Executar os testes e gerar cobertura HTML
.PHONY: test
test: clean-cov
	$(PYTEST) $(COVOPTS)
	
# Limpar o ambiente
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
