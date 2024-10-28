from flask import Flask
from flask_pymongo import PyMongo
from .config import Config  # Ensure config.py is in the same directory
from .routes import user_bp   # Ensure routes.py is in the same directory

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize PyMongo
    mongo.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(user_bp, url_prefix="/api/users")
    
    return app
