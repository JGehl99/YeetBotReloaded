import discord
from discord.ext import commands


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_role('Mods' or 'Admins')
    async def roles(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        await ctx.send('{0} joined on {0.joined_at}'.format(member))

    @commands.command(pass_context=True)
    @commands.has_role('Mods' or 'Admins')
    async def test(self, ctx, *, arg=None):
        if arg:
            await ctx.send(arg)
        else:
            print("Test with no args")

