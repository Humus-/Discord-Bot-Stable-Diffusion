import discord
import os
# from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import random
import ai_group
import logging
import yaml
from utils.utils import createUrl

from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CONFIG_PATH = "utils/config.yml"

intents = discord.Intents.default()
intents.message_content = True
config = None
# bot = commands.Bot(command_prefix='>', intents=intents)


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def load_config():
    with open(CONFIG_PATH, "r") as stream:
        try:
            global config
            config = yaml.safe_load(stream)

            logger.info("Config Loaded")
        except yaml.YAMLError as exc:
            logger.error("Could not load config file")

load_config()
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

@client.event
async def on_error(event, *args, **kwargs):
    print(f'error: {event}')
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

# bot = commands.Bot(command_prefix='!', intents = intents)

# tree = app_commands.CommandTree(client)
# @client.tree.command(name="test", description="Test to see if slash commands are working")
# async def test(interaction):
#     await interaction.response.send_message("Test")

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


@client.command(name='divs')
async def divs(ctx):
    response = "Yo cutie. Waccha up to?"
    await ctx.send(response)

@client.tree.command(guild=MY_GUILD)
async def slash(interaction: discord.Interaction, number: int, string: str):
    await interaction.response.send_message(f'Modify {number=} {string=}', ephemeral=True)

client.tree.add_command(ai_group.AIgroup(client, config), guild=MY_GUILD)

if __name__ == '__main__':
    # logger.info('Starting Bot')
    client.run(TOKEN)