from flask import Flask
from flask_pymongo import PyMongo
from .config import Config  
from .routes import user_bp   

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)
    
    app.register_blueprint(user_bp, url_prefix="/api/users")
    
    return app
