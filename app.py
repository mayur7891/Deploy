from app import create_app 
from flask import jsonify, request
from app.routes.ml_routes import ml_bp
from app.routes.comment_routes import comment_bp
from app.routes.video_routes import video_bp
from app.routes.auth_routes import user_bp

from app.services.preprocessing import preprocess_text, analyze_sentiment
from app.model import SentimentModel, CommentModel
import datetime
from datetime import timezone


from app import socketio

app = create_app()


# @app.route("/api")
# def get_data():
#     return jsonify({"message": "Hello from Flask!", "status": "success"})

# app.register_blueprint(ml_bp, url_prefix="/ml")
# app.register_blueprint(comment_bp, url_prefix="/comments")
# app.register_blueprint(video_bp, url_prefix='/video')
# app.register_blueprint(user_bp, url_prefix='/auth')

if __name__ == "__main__":
    socketio.run(app, debug=True) 
