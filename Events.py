from discord.ext import commands
import discord
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
        print(self.bot.guilds)
        print('Message from {0.author}: {0.content}'.format(message))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == cfg['roles_msg_id']:
            for name in cfg['emoji']:
                if payload.emoji.name == name:
                    role = discord.utils.get(payload.member.guild.roles, name=cfg['emoji'][name])
                    print(payload.member.name, 'has been given the role', role.name)
                    await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == cfg['roles_msg_id']:
            for name in cfg['emoji']:
                if payload.emoji.name == name:
                    guild = next(x for x in self.bot.guilds if x.id == payload.guild_id)
                    member = next(n for n in guild.members if n.id == payload.user_id)
                    role = discord.utils.get(member.guild.roles, name=cfg['emoji'][name])
                    print(member.name, 'has lost the role', role)
                    await member.remove_roles(role)
