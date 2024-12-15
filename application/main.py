import os
import discord

from application.utils.logger import Logger
from application.database.main import Database

class Application(discord.Bot):
    def __init__(self):
        super().__init__()

        self.instance = super()
        self.database = Database(self)
        Logger.info("Application initialisée. Chargement des modules...")

    async def on_ready(self):
        """Événement déclenché lorsque l'application est prête."""
        Logger.success(f"{self.user} a été correctement démarré.")
        await self.load_modules()

    async def load_modules(self):
        """Charge dynamiquement les modules (extensions)."""
        for filename in os.listdir("./application/modules"):
            if filename.endswith(".py"):
                module_name = f"application.modules.{filename[:-3]}"  # Retire ".py"
                try:
                    # Charge chaque module individuellement
                    await self.load_extension(module_name)
                    Logger.success(f"Module {module_name} chargé avec succès.")
                except Exception as e:
                    Logger.error(f"Chargement du module '{module_name}' échoué : {e}")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        if message.content.startswith("!ping"):
            await message.channel.send("Pong!")
