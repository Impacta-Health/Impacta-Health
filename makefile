up:
	docker-compose up project impacta_db mailhog

down:
	docker-compose down

exec:
	@docker-compose exec project $(cmd)

build:
	echo "Copying environment variable file."
	cp contrib/env-sample .env
    
	@echo "Starting server"
	docker-compose build

compile:
	@rm -f requirements.txt
	@rm -f dev-requirements.txt
	@make exec cmd="pip-compile -o requirements.txt pyproject.toml"
	@make exec cmd="pip-compile --extra dev -o dev-requirements.txt pyproject.toml"

compile-dev:
	@rm -f dev-requirements.txt
	@make exec cmd="pip-compile --extra dev -o dev-requirements.txt pyproject.toml"

sync:
	@make exec cmd="pip-sync dev-requirements.txt"

sh:
	@make exec cmd="bash"

shell:
	@make exec cmd="./manage.py shell_plus --plain"

setup:
	@echo "Setting up the backend..."
	@echo "Running migrations"
	@make exec cmd="./manage.py makemigrations"
	@make exec cmd="./manage.py migrate"


back-formatter:
	@echo "Formatting code accord Pep8 Style..."

	@echo "Sorting Imports..."
	@make exec cmd="isort --force-alphabetical-sort-within-sections ."

	@echo "Formatting code..."
	@make exec cmd="black ."

	@echo "Running flake8"
	@make exec cmd="flake8"

	@echo "Completed with 0 erros"


