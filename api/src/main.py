import os
from flask import Flask
from dotenv import load_dotenv
from app.routes.init_routes import init_routes
from app.models.db import db  # Importer l'instance de db
from app.models.items import Item

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Créer l'application Flask
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_BACEUGEU_DB")  # Chargement depuis .env
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialiser la base de données
db.init_app(app)
with app.app_context():
    # Créer toutes les tables
    db.create_all()

    # Insérer les items initiaux
    if not Item.query.first():  # Vérifier s'il y a déjà des items dans la base
        Item.create_initial_items()

# Initialiser les routes
init_routes(app)

if __name__ == "__main__":
    # app.run(debug=os.getenv("FLASK_DEBUG", False))
    app.run(port=8080)  # Changez le port ici
