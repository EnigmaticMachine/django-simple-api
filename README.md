# Simple API

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Environment Variables](#environment-variables)
  - [Build and Run](#makefile-commands)
- [Running Tests](#makefile-commands)
- [Makefile Commands](#makefile-commands)
- [Docker Configuration](#docker-configuration)
- [Testing Data Import and Verification](#testing-data-import-and-verification)

## Introduction

This project is a Django-based application with a REST API. The project includes models, serializers, views, and tests.

In the root of the project, you will find the `Makefile`. This file is designed to be the primary point for running the application and tests. While it is possible to use Docker Compose or the Dockerfile directly, the `Makefile` is intended to streamline the setup and execution of various tasks with a single command.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Use command `make init` to create a `.env` file in the root directory:

```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_SUPERUSER_USERNAME=username
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=supersecretpassword

DATABASE_URL=postgres://myuser:mypassword@db:5432/mydatabase
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_ENV=dev
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1],backend
```

And `.env.test` file in the root directory:

```
DJANGO_ENV=test
DEBUG=True
```

## Makefile Commands

In the root of the project, you will find the `Makefile`. This file is designed to be the primary point for running the application and tests. While it is possible to use Docker Compose or the Dockerfile directly, the `Makefile` is intended to streamline the setup and execution of various tasks with a single command.

The `Makefile` contains various commands to simplify common tasks:

- `make help`: Show help message.
- `make init`: Initialize the environment.
- `make build`: Build the Docker images for development.
- `make up`: Start the Docker containers for development.
- `make down`: Stop the Docker containers for development.
- `make logs`: Follow logs of Docker containers for development.
- `make migrate`: Run database migrations for development.
- `make createsuperuser`: Create a superuser for development.
- `make import-verify`: Run the import and verification script.
- `make shell`: Open a Django shell for development.
- `make clean`: Clean up Docker containers, images, and volumes for development.
- `make test-build`: Build the Docker images for testing.
- `make test-up`: Start the Docker containers for testing.
- `make test-down`: Stop the Docker containers for testing.
- `make test-logs`: Follow logs of Docker containers for testing.
- `make test-run`: Run tests.
- `make test-run-debug`: Run tests with debug logs.
- `make test-shell`: Open a Django shell for testing.
- `make test-clean`: Clean up Docker containers, images, and volumes for testing.

### Build and Run

1. Build the Docker images:
   docker-compose build

2. Start the Docker containers:
   docker-compose up

3. The application will be available at `http://localhost:8000`.

## Running Tests

1. Build the test Docker image:
   docker-compose -f docker-compose.test.yml build

2. Run the tests:
   docker-compose -f docker-compose.test.yml up

## Docker Configuration

### Dockerfile

The `Dockerfile` sets up the environment for the Django application, installs dependencies, and copies the project files.

### Docker Compose

- `docker-compose.yml`: Defines the services for the development environment, including the Django application and PostgreSQL database.
- `docker-compose.test.yml`: Defines the services for the testing environment.

## Testing Data Import and Verification

To test the data import and verify the endpoints, you can use Makefile command.

### Usage

Execute the following Makefile command:

`make import-verify`

The command will run a script that imports test data and verifies the catalog, attribute, and product endpoints.
