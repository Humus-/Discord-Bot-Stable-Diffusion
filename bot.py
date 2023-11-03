# bot.py
# import os

# import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# intents = discord.Intents.default()
# print(f'default Intents: {intents}')
# client = discord.Client(intents = intents)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# client.run(TOKEN)



import discord
import os
# from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import random

from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
# bot = commands.Bot(command_prefix='>', intents=intents)

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# bot.run(TOKEN)



# async with aiohttp.ClientSession() as session:
#     async with session.get('http://aws.random.cat/meow') as r:
#         if r.status == 200:
#             js = await r.json()
#             await channel.send(js['file'])

MY_GUILD = discord.Object(id=167319816649179149)
class CustomClient(commands.Bot):
    async def on_ready(self):
        await self.tree.sync(guild=MY_GUILD)

        # tree = app_commands.CommandTree(self)
        # print(f'client tree: {tree}')

        for guild in self.guilds:
            print(f'guild name: {guild}, id: {guild.id}')
            for channel in guild.channels:
                print(f'channel name: {channel}, id: {channel.id}')
        # client.channels.cache.get('CHANNEL ID').send('Hello here!');

        # 167319816649179149

        g_channel = self.get_channel(167319816649179149);

        # await g_channel.send('Hello here!');

        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        print(f'message: {message.content}')

        if message.content == 'pinga':
            await message.channel.send('pong')

        if message.content == 'raise exception':
            raise discord.DiscordExceptio

        if message.content == 'show image':
            print('showing image')
            await message.channel.send(file = discord.File('stable-diffusion-images-generation.png'))


        await self.process_commands(message)

# switch between these 2 as activity to mess with people
watching = discord.Activity(name='you intently', type = discord.ActivityType.watching)
playing = discord.Game(name='with life')
client = CustomClient(intents = intents, command_prefix = '!', activity = watching)  # or activity = playing

# @client.event
# async def on_error(event, *args, **kwargs):
#     print(f'error: {event}')
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

# bot = commands.Bot(command_prefix='!', intents = intents)

# tree = app_commands.CommandTree(client)
@client.tree.command(name="test", description="Test to see if slash commands are working")
async def test(interaction):
    await interaction.response.send_message("Test")

@client.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

# @client.slash_command(name="test", guild_ids=[167319816649179149]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
# async def first_slash(ctx): 
#     await ctx.respond("You executed the slash command!")

client.run(TOKEN)