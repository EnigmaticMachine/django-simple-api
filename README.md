# Simple API

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Environment Variables](#environment-variables)
  - [Build and Run](#build-and-run)
- [Running Tests](#running-tests)
- [Makefile Commands](#makefile-commands)
- [Docker Configuration](#docker-configuration)
- [Contact](#contact)

## Introduction

This project is a Django-based application with a REST API. The project includes models, serializers, views, and tests.

In the root of the project, you will find the `Makefile`. This file is designed to be the primary point for running the application and tests. While it is possible to use Docker Compose or the Dockerfile directly, the `Makefile` is intended to streamline the setup and execution of various tasks with a single command.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

DJANGO_SECRET_KEY=your_secret_key
DJANGO_SUPERUSER_USERNAME=your_admin_username
DJANGO_SUPERUSER_EMAIL=your_admin_email@example.com
DJANGO_SUPERUSER_PASSWORD=your_admin_password
DATABASE_URL=postgres://username:password@postgres:5432/dbname

Create a `.env.test` file in the root directory of your project and add the following environment variables:

DJANGO_ENV=test
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1],backend,nginx

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
