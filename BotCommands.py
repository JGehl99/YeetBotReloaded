import discord
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup as bs
import requests
from Minesweeper import Minesweeper


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_role('Admins')
    async def roles(self, ctx, args=None):
        member = find_member(ctx, args)
        if not member:
            await ctx.send('User not found!')
            return

        roles = member.name + '\'s Roles:\n\n'
        for role in member.roles:
            roles += '`' + role.name + '`' + '\n'
        await ctx.send(roles)

    @commands.command(pass_context=True)
    @commands.has_role('Admins')
    async def test(self, ctx, *, arg=None):
        if arg:
            await ctx.send(arg)
        else:
            print("Test with no args")

    @commands.command(pass_context=True)
    async def minesweeper(self, ctx, *, arg=None):
        x = 0
        y = 0
        mines = 0
        try:
            args = str(arg).split()
            print(args)
            x = int(args[0])
            y = int(args[1])
            mines = int(args[2])
        except (TypeError, ValueError):
            return await ctx.send("Usage: `!Minesweeper <width> <height> <# of mines>`")

        ms = Minesweeper(x, y, mines)
        return await ctx.send(ms.msg)

    @commands.command(pass_context=True)
    @commands.has_role('Admins')
    async def add_reaction(self, ctx, channel, emoji, msg_id):
        channel_ = get(ctx.guild.channels, name=channel)
        message = await channel_.fetch_message(msg_id)
        await message.add_reaction(emoji)

    @commands.command(pass_context=True)
    @commands.has_role('Admins')
    async def remove_reaction(self, ctx, channel, emoji, msg_id):
        channel_ = get(ctx.guild.channels, name=channel)
        message = await channel_.fetch_message(msg_id)
        await message.remove_reaction(emoji, get(ctx.guild.members, id=802242499107225610))

    @commands.command(pass_context=True)
    async def steam(self, ctx, *, arg=None):
        if arg:
            msg = str(arg).replace(' ', '+')
            search_page_request = requests.get("https://store.steampowered.com/search/?term=" + msg + "&category1=998")
            search_page = bs(search_page_request.content, features="lxml")
            game_link = search_page.find('a', class_='search_result_row ds_collapse_flag').get('href')
            game_title = search_page.find('span', class_='title').text

            game_page_request = requests.get(game_link)
            game_page = bs(game_page_request.content, features='lxml')
            game_img_src = game_page.find('img', class_='game_header_image_full').get('src')
            game_desc = game_page.find('div', class_='game_description_snippet').text.strip()
            game_price_div = game_page.find('div', class_='game_area_purchase_game_wrapper')
            game_price = game_price_div.find('div', class_='game_purchase_price price').text.strip()
            print(game_price)
            rich_embed = discord.Embed(title=game_title, description=game_link)
            rich_embed.set_image(url=game_img_src)
            rich_embed.add_field(name=game_price, value=game_desc)

            await ctx.send(embed=rich_embed)


# Finds member in guild, else return None, if name is empty, return author member
def find_member(ctx, name):
    if not name: return ctx.author
    member = [x for x in ctx.guild.members
              if x.name == name or x.nick == name or (x.name + '#' + x.discriminator) == name]
    return member[0] if member else None
