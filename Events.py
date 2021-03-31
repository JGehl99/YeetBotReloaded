from discord.ext import commands
from config import config as cfg
from discord.utils import get


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
        if message.author is not self.bot:
            print('Message From ', message.author, ':', message.content)
            if message.attachments:
                print('\n', message.attachments[0].url, '\n')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = get(member.guild.roles, name=cfg['new_user_role'])
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # Rules Msg
        if payload.message_id == cfg['rules_msg_id']:
            if not get(payload.member.roles, name=cfg['new_user_role']):
                print('User is already verified!')
                await remove_reaction(payload)
                return
            if payload.emoji.name == cfg['emoji'][payload.emoji.name][0]:
                await add_role(payload.member, cfg['emoji'][payload.emoji.name][1])
                await remove_reaction(payload)
                await remove_role(payload.member, cfg['new_user_role'])

        if payload.message_id == cfg['roles_msg_id']:
            if payload.emoji.name == cfg['emoji'][payload.emoji.name][0]:
                await add_role(payload.member, cfg['emoji'][payload.emoji.name][1])

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == cfg['roles_msg_id']:
            if payload.emoji.name == cfg['emoji'][payload.emoji.name][0]:
                guild = get(self.bot.guilds, id=payload.guild_id)
                member = get(guild.members, id=payload.user_id)
                await remove_role(member, cfg['emoji'][payload.emoji.name][1])


async def add_role(member, role_name):
    role = get(member.guild.roles, name=role_name)
    print(member.name, 'has been given the role', role_name)
    await member.add_roles(role)


async def remove_role(member, role_name):
    role = get(member.guild.roles, name=role_name)
    print(member.name, 'has lost the role', role)
    await member.remove_roles(role)


async def remove_reaction(payload):
    channel = get(payload.member.guild.channels, id=payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    await message.remove_reaction(payload.emoji.name, payload.member)
