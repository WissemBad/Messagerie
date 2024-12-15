class User:
    def __init__(self, database):
        self.database = database

    async def create(self, username, avatar, grade, is_banned):
        """Insère un utilisateur dans la base de données."""
        query = """INSERT INTO Utilisateur (username, avatar, grade, is_banned) 
                   VALUES (%s, %s, %s, %s)"""
        params = (username, avatar, grade, is_banned)
        return await self.database.query(query, params)

    async def exists(self, user_id):
        """Vérifie l'existence d'un utilisateur dans la base de données."""
        query = "SELECT 1 FROM Utilisateur WHERE id = %s"
        result = await self.database.fetch_one(query, (user_id,))
        return True if result else False

    async def get_by_id(self, user_id):
        """Récupère un utilisateur par ID dans la base de données."""
        query = "SELECT * FROM Utilisateur WHERE id = %s"
        result = await self.database.fetch_one(query, (user_id,))
        return result

    async def update(self, user_id, username=None, avatar=None, grade=None, is_banned=None):
        """Met à jour les informations d'un utilisateur par ID dans la base de données."""
        set_clauses = []
        params = []

        if username is not None: set_clauses.append("username = %s"), params.append(username)
        if avatar is not None: set_clauses.append("avatar = %s"), params.append(avatar)
        if grade is not None: set_clauses.append("grade = %s"), params.append(grade)
        if is_banned is not None: set_clauses.append("is_banned = %s"), params.append(is_banned)
        if not set_clauses: return False

        set_clause = ", ".join(set_clauses)
        query = f"UPDATE Utilisateur SET {set_clause} WHERE id = %s"
        params.append(user_id)
        return await self.database.query(query, tuple(params))

    async def delete(self, user_id):
        """Supprime un utilisateur par ID dans la base de données."""
        query = "DELETE FROM Utilisateur WHERE id = %s"
        return await self.database.query(query, (user_id,))
