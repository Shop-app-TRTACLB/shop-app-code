# Étape 1 : Utiliser une image de base Python
FROM python:3.9-slim

# Étape 2 : Installer les dépendances système pour pyodbc et le pilote ODBC pour SQL Server
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    gcc \
    g++ \
    curl \
    gnupg \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

# Étape 3 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 4 : Copier les fichiers de requirements.txt et installer les dépendances
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Copier le code source de l'application dans le conteneur
COPY app /app/app
COPY main.py /app/main.py

# Étape 6 : Définir les variables d'environnement
ENV FLASK_APP=main.py   
ENV FLASK_ENV=development  
ENV PRIVATE_ENDPOINT_IP=${PRIVATE_ENDPOINT_IP}
ENV SQL_CONNECTION_STRING=${SQL_CONNECTION_STRING}
ENV SECRET_KEY=${SECRET_KEY}

# Étape 7 : Exposer le port utilisé par Flask (5000 par défaut)
EXPOSE 5000

# Étape 8 : Lancer l'application Flask
CMD ["flask", "run", "--host=0.0.0.0"]
