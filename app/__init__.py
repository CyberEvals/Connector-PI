from flask import Flask
from app.api.docs import api

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
    
    # Initialize the API
    api.init_app(app)
    
    return app 