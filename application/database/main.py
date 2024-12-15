import aiomysql
import asyncio

from application.utils.logger import Logger
from configs.main import DB_HOST, DB_NAME, DB_PASS, DB_USER

class Database:
    def __init__(self, app):
        self.app = app
        self.connection = None
        self.cursor = None

    async def connect(self):
        """Établit une connexion asynchrone à la base de données"""
        try:
            self.connection = await aiomysql.connect(
                host=DB_HOST,
                port=3306,
                user=DB_USER,
                password=DB_PASS,
                db=DB_NAME
            )
            self.cursor = await self.connection.cursor()
            Logger.success("Connexion asynchrone à la base de données établie")
        except Exception as e:
            Logger.error(f"Erreur de connexion à la base de données : {e}")
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
        except Exception as e:
            Logger.warning(f"Exécution de la requête non réussie : {e}")
            await self.connection.rollback()

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

    async def create_user(self, username, avatar, grade, is_banned):
        """Exemple pour insérer un utilisateur dans la base de données de manière asynchrone"""
        query = """INSERT INTO Utilisateur (username, avatar, grade, is_banned) 
                   VALUES (%s, %s, %s, %s)"""
        params = (username, avatar, grade, is_banned)
        await self.query(query, params)

    async def get_user_by_id(self, user_id):
        """Exemple pour récupérer un utilisateur par ID de manière asynchrone"""
        query = "SELECT * FROM Utilisateur WHERE id = %s"
        result = await self.fetch_one(query, (user_id,))
        return result

# Exemple d'utilisation de la classe Database dans une application
async def main():
    db = Database(None)  # 'None' ici, mais tu peux y passer ton app si nécessaire
    await db.connect()

    # Exemple d'ajout d'un utilisateur
    await db.create_user('JohnDoe', 'https://example.com/avatar.png', 'admin', False)

    # Exemple de récupération d'un utilisateur par ID
    user = await db.get_user_by_id(1)
    if user:
        print(f"Utilisateur récupéré : {user}")

    # Fermer la connexion à la base de données
    await db.close()

# Démarre l'application asynchrone
if __name__ == "__main__":
    asyncio.run(main())
