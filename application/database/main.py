import aiomysql

from application.database import user # profile, email
from application.utils.logger import Logger
from configs.main import DB_USER, DB_PASS, DB_NAME, DB_HOST

class Database:
    def __init__(self, app):
        self.app = app
        self.connection = None
        self.cursor = None

        # Modules
        self.user = user.User(self)
        self.profile = None
        self.email = None

    async def connect(self):
        """Établit une connexion asynchrone à la base de données"""
        Logger.info("Connexion à la base de données...")
        try:
            self.connection = await aiomysql.connect(
                host=DB_HOST,
                port=3306,
                user=DB_USER,
                password=DB_PASS,
                db=DB_NAME
            )
            self.cursor = await self.connection.cursor()
            Logger.success("Connexion à la base de données établie")
        except Exception as e:
            Logger.error(f"Connexion à la base de données échouée : {e}")
            raise e

    async def close(self):
        """Ferme la connexion asynchrone à la base de données"""
        if self.connection:
            await self.cursor.close()
            self.connection.close()
            Logger.info("Connexion à la base de données fermée")
            return True
        return False

    async def query(self, query, params=None):
        """Exécute une requête SQL (INSERT, UPDATE, DELETE) de manière asynchrone"""
        try:
            await self.cursor.execute(query, params or ())
            await self.connection.commit()
            Logger.info("Requête exécutée avec succès")
            return True
        except Exception as e:
            Logger.warning(f"Exécution de la requête non réussie : {e}")
            await self.connection.rollback()
            return False

    async def fetch_one(self, query, params=None):
        """Récupère une seule ligne de résultats d'une requête SELECT de manière asynchrone"""
        try:
            await self.cursor.execute(query, params or ())
            result = await self.cursor.fetchone()
            return result
        except Exception as e:
            Logger.warning(f"Récupération des données non réussie : {e}")
            return None

    async def fetch_all(self, query, params=None):
        """Récupère toutes les lignes de résultats d'une requête SELECT de manière asynchrone"""
        try:
            await self.cursor.execute(query, params or ())
            result = await self.cursor.fetchall()
            return result
        except Exception as e:
            Logger.warning(f"Récupération des données non réussie : {e}")
            return []