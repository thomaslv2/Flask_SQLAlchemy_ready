from flask import Flask
from .views.users import user


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user)

    return app
