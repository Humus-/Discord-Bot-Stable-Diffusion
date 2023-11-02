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

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
# bot = commands.Bot(command_prefix='>', intents=intents)

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# bot.run(TOKEN)

class CustomClient(discord.Client):
    async def on_ready(self):

        for guild in client.guilds:
            print(f'guild name: {guild}, id: {guild.id}')
            for channel in guild.channels:
                print(f'channel name: {channel}, id: {channel.id}')
        # client.channels.cache.get('CHANNEL ID').send('Hello here!');

        # 167319816649179149

        g_channel = client.get_channel(167319816649179149);

        await g_channel.send('Hello here!');

        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        # don't respond to ourselves
        # if message.author == self.user:
        #     return

        if message.content == 'pinga':
            await message.channel.send('pong')



client = CustomClient(intents = intents)
# print(f'all channels: {client.get_all_channels()}')

client.run(TOKEN)