import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_name="development"):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    
    # Setup JWT
    jwt.init_app(app)
    
    # Setup CORS
    CORS(app)
    
    #Bind Flask-Migrate to app
    migrate.init_app(app, db)

    @app.route('/')
    def hello():
        return 'This is flask RestFul API'

    # Import and register blueprints
    from app.auth.route import auth_blueprint
    from app.blog_post.route import blog_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint, url_prefix='/')
    return app
