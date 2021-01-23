from discord.ext import commands
from config import config as cfg

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == cfg['roles_msg_id']:
            print(payload)

