import discord
import os

from utils.console import Console
from configs import main as configuration

Console.info("Démarrage de l'application initialisé...")
Client = discord.Bot()

@Client.event
async def on_ready():
    Console.success(f"{Client.user} a été correctement démarré.")

@Client.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

Client.run(configuration.CL_TOKEN)