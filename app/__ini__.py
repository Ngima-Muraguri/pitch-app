from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import create_engine, engine
import psycopg2, os
from app.config import config_options

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from app.auth.routes import auths
    from app.main.routes import main
    from app.errors.handlers import errors
    app.register_blueprint(auths)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app