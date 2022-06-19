import logging
from flask import Flask
from flask_login import LoginManager

from allabouttravel_app.db import db
from allabouttravel_app.admin.views import blueprint as admin_blueprint
from allabouttravel_app.place.views import blueprint as place_blueprint
from allabouttravel_app.user.models import User
from allabouttravel_app.user.views import blueprint as user_blueprint


logging.basicConfig(filename='app.log', level=logging.INFO)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(place_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
