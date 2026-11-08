from flask import Blueprint, jsonify, current_app
from redis.exceptions import RedisError

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to my Flask API!"
    })


@api.route("/health", methods=["GET"])
def health():
    redis_client = current_app.config["REDIS_CLIENT"]

    try:
        redis_client.ping()

        return jsonify({
            "status": "healthy",
            "redis": "connected"
        }), 200

    except RedisError:
        return jsonify({
            "status": "unhealthy",
            "redis": "disconnected"
        }), 503


@api.route("/info", methods=["GET"])
def info():
    return jsonify({
        "application": "docker-flask-redis",
        "version": current_app.config["APP_VERSION"]
    })
