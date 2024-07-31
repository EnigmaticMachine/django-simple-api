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
	@chmod +x ./scripts/entrypoint.sh || (echo "Failed to set permissions for ./scripts/entrypoint.sh" && exit 1)
	@chmod +x ./scripts/test_import_and_verify.sh || (echo "Failed to set permissions for ./scripts/test_import_and_verify.sh" && exit 1)
	@if [ ! -f .env ]; then \
		echo "DJANGO_SECRET_KEY=your-secret-key" > .env; \
		echo "DJANGO_SUPERUSER_USERNAME=username" >> .env; \
		echo "DJANGO_SUPERUSER_EMAIL=admin@example.com" >> .env; \
		echo "DJANGO_SUPERUSER_PASSWORD=supersecretpassword" >> .env; \
		echo "DATABASE_URL=postgres://myuser:mypassword@db:5432/mydatabase" >> .env; \
		echo "POSTGRES_DB=mydatabase" >> .env; \
		echo "POSTGRES_USER=myuser" >> .env; \
		echo "POSTGRES_PASSWORD=mypassword" >> .env; \
		echo "POSTGRES_HOST=db" >> .env; \
		echo "POSTGRES_PORT=5432" >> .env; \
		echo "DJANGO_ENV=dev" >> .env; \
		echo "DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1],backend" >> .env; \
		echo ".env file created"; \
	else \
		echo ".env file already exists"; \
	fi
	@if [ ! -f .env.test ]; then \
		echo "DJANGO_ENV=test" > .env.test; \
		echo "DEBUG=True" >> .env.test; \
		echo ".env.test file created"; \
	else \
		echo ".env.test file already exists"; \
	fi
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


.PHONY: import-verify
import-verify: ## Run the import and verification script
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans
	$(DC) -f $(COMPOSE_FILE) build
	$(DC) -f $(COMPOSE_FILE) up -d
	sleep 5
	@scripts/test_import_and_verify.sh

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
