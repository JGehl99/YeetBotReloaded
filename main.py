from config import config as cfg
import discord
from discord.ext import commands
from BotCommands import BotCommands
from Events import Events


intents = discord.Intents.default()
intents.reactions = True
intents.members = True
desc = ''

bot = commands.Bot(command_prefix='!', description=desc, intents=intents)

bot.add_cog(BotCommands(bot))
bot.add_cog(Events(bot))

bot.run(cfg['token'])
