"""MyPass app factory"""

import os
import typing

from flask import Flask

from mypass import db


def create_app(test_config: dict[str, typing.Any] | None = None) -> Flask:
    """MyPass application factory"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "mypass.sqlite"))

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    db.init_app(app)

    return app
