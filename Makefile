# Variables
DC = docker-compose
COMPOSE_FILE = docker-compose.yml
TEST_COMPOSE_FILE = docker-compose.test.yml


# Default target
.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: init
init: ## Init environment
	@echo "Initializing environment..."
	@chmod +x ./entrypoint.sh || (echo "Failed to set permissions for /code/entrypoint.sh" && exit 1)
	@if [ ! -f .env ]; then echo ".env file does not exist"; fi
	@if [ ! -f .env.test ]; then echo ".env.test file does not exist"; fi
	@echo "Environment initialized."

# devlopment targets
.PHONY: build
build: ## Build the Docker images for devlopment
	$(DC) -f $(COMPOSE_FILE) build

.PHONY: up
up: ## Start the Docker containers for devlopment
	$(DC) -f $(COMPOSE_FILE) up -d

.PHONY: down
down: ## Stop the Docker containers for devlopment
	$(DC) -f $(COMPOSE_FILE) down

.PHONY: logs
logs: ## Follow logs of Docker containers for devlopment
	$(DC) -f $(COMPOSE_FILE) logs -f

.PHONY: migrate
migrate: ## Run database migrations for devlopment
	$(DC) -f $(COMPOSE_FILE) run backend python manage.py makemigrations
	$(DC) -f $(COMPOSE_FILE) run backend python manage.py migrate

.PHONY: createsuperuser
createsuperuser: ## Create a superuser for devlopment
	$(DC) -f $(COMPOSE_FILE) run backend python manage.py createsuperuser

.PHONY: shell
shell: ## Open a Django shell for devlopment
	$(DC) -f $(COMPOSE_FILE) run backend python manage.py shell

.PHONY: clean
clean: ## Clean up Docker containers, images, and volumes for devlopment
	$(DC) -f $(COMPOSE_FILE) down -v --rmi all --remove-orphans

# Testing targets
.PHONY: test-build
test-build: ## Build the Docker images for testing
	$(DC) -f $(TEST_COMPOSE_FILE) build

.PHONY: test-up
test-up: ## Start the Docker containers for testing
	$(DC) -f $(TEST_COMPOSE_FILE) up -d

.PHONY: test-down
test-down: ## Stop the Docker containers for testing
	$(DC) -f $(TEST_COMPOSE_FILE) down

.PHONY: test-logs
test-logs: ## Follow logs of Docker containers for testing
	$(DC) -f $(TEST_COMPOSE_FILE) logs -f

.PHONY: test-run
test-run: ## Run tests
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans
	$(DC) -f $(TEST_COMPOSE_FILE) build
	$(DC) -f $(TEST_COMPOSE_FILE) up -d
	$(DC) -f $(TEST_COMPOSE_FILE) run backend pytest
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: test-run-debug
test-run-debug: ## Run tests
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans
	$(DC) -f $(TEST_COMPOSE_FILE) build
	$(DC) -f $(TEST_COMPOSE_FILE) up -d
	$(DC) -f $(TEST_COMPOSE_FILE) run backend pytest --log-cli-level=DEBUG
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: test-shell
test-shell: ## Open a Django shell for testing
	$(DC) -f $(TEST_COMPOSE_FILE) run backend python manage.py shell

.PHONY: test-clean
test-clean: ## Clean up Docker containers, images, and volumes for testing
	$(DC) -f $(TEST_COMPOSE_FILE) down -v --rmi all --remove-orphans
