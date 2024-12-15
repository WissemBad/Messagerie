import os
import discord

from application.utils.logger import Logger
from application.database.main import Database

class Application(discord.Bot):
    def __init__(self, client):
        super().__init__(
            intents=client.configuration['intents'],
            activity=client.configuration['activity'],
            status=client.configuration['status'],

            loop=client.configuration['loop'],
            proxy=client.configuration['proxy'],
        )

        self.instance = super()
        self.database = Database(self)

        Logger.info("Démarrage de l'application en cours...")

    async def on_ready(self):
        """Événement déclenché lorsque l'application est prête."""
        await self.database.connect()
        await self.load_modules()
        Logger.success(f"{self.user} est prêt et opérationnel.")

    async def load_modules(self):
        """Charge dynamiquement les modules."""
        Logger.info("Chargement des modules...")
        try:
            for filename in os.listdir("./application/modules"):
                if filename.endswith(".py"):
                    module_name = f"application.modules.{filename[:-3]}"
                    try:
                        self.load_extension(module_name)
                        print(f"  → Module {module_name} chargé.")
                    except Exception as error:
                        Logger.warning(f"Chargement du module '{module_name}' échoué.\n{error}")

            Logger.success("Tous les modules ont été correctement chargés.")

        except Exception as error:
            return Logger.error(f"Chargement des modules non réussi :\n{error}")

    async def on_interaction(self, interaction: discord.Interaction):
        if not await self.database.user.exists(interaction.user.id) and interaction.id != "caca":
            return await interaction.message.channel.send("> Verification error")

    async def on_message(self, message: discord.Message):
        if message.author == self.user: return
        if not await self.database.user.exists(message.author.id): return
        await message.reply(message.content, mention_author=False)
