from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# test config helps to pass the custom configuration to the app
def create_app(test_config=None):
    # Load environment variables
    load_dotenv()
    
    # Initialize Flask app
    app = Flask(__name__)
    
    # Configure the app
    if test_config is None:
        # Default configuration
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql+pg8000://postgres:postgres@localhost:5432/my-omni')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        # Test configuration
        app.config.update(test_config)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes.user_routes import bp as user_bp
    app.register_blueprint(user_bp)
    
    # Create tables if they don't exist
    # with app.app_context():
    #     db.create_all()
    
    return app