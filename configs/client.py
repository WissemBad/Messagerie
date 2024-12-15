import discord

class Client:
    def __init__(self):
        self.intents = discord.Intents.all()

        self.activity = discord.Activity(type=discord.ActivityType.watching, name="Solve SCP ・ Messagerie")
        self.status = discord.Status.idle

        self.shard_id = 0
        self.shard_count = 2

        self.loop = None
        self.proxy = None

        self.configuration = self.configuration()

    def configuration(self):
        return vars(self)
