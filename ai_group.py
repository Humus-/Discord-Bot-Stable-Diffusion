import discord
from discord import app_commands
from discord.ext import commands
from utils.utils import createUrl

import aiohttp

class AIgroup(app_commands.Group):
    """Manage general commands"""
    def __init__(self, bot: commands.Bot, config):
        print(f'comfig yyep {type(config)}')
        super().__init__()
        self.name = "ai"
        self.bot = bot
        self.config = config

    @app_commands.command(name = 'chat')
    async def hello(self, interaction: discord.Interaction):
        # await interaction.response.send_message('Hello')

        async with aiohttp.ClientSession() as session:
            service_url = createUrl(self.config['model_server']['chat_server'], self.config['model_server']['chat_port'], self.config['model_server']['chat_uri'])
            async with session.get(service_url) as r:
                print(r)
                if r.status == 200:
                    # js = await r.json()
                    return await interaction.response.send_message('Bullah di jana mai kaun')
                    # await channel.send(js['file'])
                else:
                    return await interaction.response.send_message('Uff teri galti...')


    @app_commands.command()
    async def dream(self, interaction: discord.Interaction):
        """tells you what version of the bot software is running."""
        await interaction.response.send_message('This is an untested test version')