import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    app_settings = os.getenv(
        'APP_SETTINGS',
        'app.config.DevelopmentConfig'
    )
    app.config.from_object(app_settings)
    
    db.init_app(app)
    
    # Setup JWT
    jwt.init_app(app)
    
    # Setup CORS
    CORS(app)

    # Import and register blueprints
    from app.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
