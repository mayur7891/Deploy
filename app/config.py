import os

class Config:
    """Configuration settings for the Flask app."""
    SECRET_KEY = os.getenv("SECRET_KEY")  # Default for local dev
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI")  # Default local MongoDB
