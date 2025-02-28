from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config import Config

from flask_socketio import SocketIO

# Initialize extensions globally
mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins="*")
  # ✅ Allow CORS for WebSockets


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize plugins
    mongo.init_app(app)
    bcrypt.init_app(app)
    CORS(app)
    jwt.init_app(app)
    socketio.init_app(app)
    
    from app.routes.ml_routes import ml_bp
    from app.routes.comment_routes import comment_bp
    from app.routes.video_routes import video_bp
    from app.routes.auth_routes import user_bp

    # Register blueprints
    app.register_blueprint(ml_bp, url_prefix="/ml")
    app.register_blueprint(comment_bp, url_prefix="/comments")
    app.register_blueprint(video_bp, url_prefix='/video')
    app.register_blueprint(user_bp, url_prefix='/auth')

    @app.route("/api")
    def get_data():
        return {"message": "Hello from Flask!", "status": "success"}

    return app
