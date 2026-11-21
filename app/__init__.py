import os

import redis
from flask import Flask

from app.routes import api


def create_app():
    app = Flask(__name__)

    app.config["APP_VERSION"] = os.getenv("APP_VERSION", "1.0.0")

    app.config["REDIS_CLIENT"] = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        decode_responses=True,
        socket_connect_timeout=2,
    )

    app.register_blueprint(api)

    return app
