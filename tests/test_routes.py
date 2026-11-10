from unittest.mock import Mock

import pytest
from redis.exceptions import RedisError

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["APP_VERSION"] = "1.0.0"

    # Mock Redis to avoid requiring a real Redis connection
    redis_mock = Mock()
    app.config["REDIS_CLIENT"] = redis_mock

    with app.test_client() as client:
        yield client, redis_mock


def test_home_route(client):
    test_client, _ = client

    response = test_client.get("/")

    assert response.status_code == 200
    assert response.json == {"message": "Welcome to my Flask API!"}


def test_health_route_redis_connected(client):
    test_client, redis_mock = client
    redis_mock.ping.return_value = True

    response = test_client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy", "redis": "connected"}


def test_health_route_redis_disconnected(client):
    test_client, redis_mock = client
    redis_mock.ping.side_effect = RedisError("Redis unavailable")

    response = test_client.get("/health")

    assert response.status_code == 503
    assert response.json == {"status": "unhealthy", "redis": "disconnected"}


def test_info_route(client):
    test_client, _ = client

    response = test_client.get("/info")

    assert response.status_code == 200
    assert response.json == {"application": "docker-flask-redis", "version": "1.0.0"}
