from flask import Flask
from database import db
from cfg import DATABASE_URL, SECRET_KEY, FLASK_DEBUG
from controllers.main_controller import main_controller
from controllers.test_controller import test_controller


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = SECRET_KEY

    app.register_blueprint(main_controller)

    if FLASK_DEBUG == "1":
        app.register_blueprint(test_controller)

    db.init_app(app)

    return app
