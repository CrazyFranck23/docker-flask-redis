# Docker Flask Redis

A containerized REST API built with Python, Flask,
Docker and Docker Compose.

## Architecture

- Flask: REST API
- Gunicorn: WSGI server
- Redis: In-memory data store
- Docker: Application containerization
- Docker Compose: Multi-container orchestration

## Prerequisites

- Git
- Docker Desktop with WSL 2 integration
- Docker Compose

## Installation

Clone the repository:

    git clone https://github.com/CrazyFranck23/docker-flask-redis.git

    cd docker-flask-redis

Create the environment file:

    cp .env.example .env

Start the application:

    docker compose up -d --build

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /health | Application and Redis health |
| GET | /info | Application information |

## Access

API: http://localhost:5000

## Useful Commands

Start:

    docker compose up -d --build

Stop:

    docker compose stop

View containers:

    docker compose ps

View logs:

    docker compose logs -f

Restart:

    docker compose restart

Stop and remove containers:

    docker compose down

Stop and remove containers and volumes:

    docker compose down -v

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| APP_VERSION | 1.0.0 | Application version |
| REDIS_HOST | redis | Redis hostname |
| REDIS_PORT | 6379 | Redis port |

## Author

Franck NOUTSA FOTSO
