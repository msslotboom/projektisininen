from os import getenv
from flask import Flask
from database import db
from cfg import DATABASE_URL, SECRET_KEY
from controller import controller


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(controller)

    db.init_app(app)

    return app
