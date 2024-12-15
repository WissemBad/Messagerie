import os
import dotenv

# Chargement du fichier d'environnement
dotenv.load_dotenv()

# Chargement des variables d'environnement
CL_TOKEN = os.getenv("TOKEN")
RUBIK_API = os.getenv("RUBIK_API")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")