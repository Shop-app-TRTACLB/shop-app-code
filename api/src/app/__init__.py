# src/app/__init__.py

import os
from flask import Flask
from dotenv import load_dotenv
from .models.db import db
from .routes.init_routes import init_routes

load_dotenv()

def create_app(testing=False):
    """Factory function pour créer l'application Flask."""
    app = Flask(__name__)

    # Si en mode test, utiliser SQLite en mémoire
    # Sinon, lire la config .env
    if testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQL_CONNECTION_STRING")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback_secret_key")
    app.config['TESTING'] = testing

    # Init DB
    db.init_app(app)
    # Enregistrer les routes
    init_routes(app)

    return app
