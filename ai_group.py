QUERY_LOG_FILE = 'query_logs.log'

import discord
from discord import app_commands
from discord.ext import commands
from utils.utils import createUrl

import logging
from logging.handlers import RotatingFileHandler

import aiohttp

class AIgroup(app_commands.Group):
    """Manage general commands"""
    def __init__(self, bot: commands.Bot, config: dict[str, any]):
        super().__init__()

        # separate logger for debugging queries.
        my_handler = RotatingFileHandler(QUERY_LOG_FILE,
            mode = 'a',
            maxBytes = 5 * 1024 * 1024,
            backupCount = 2,
            encoding = None,
            delay = 0)
        my_handler.setLevel(logging.INFO)

        q_log = logging.getLogger('query')
        q_log.setLevel(logging.INFO)
        q_log.addHandler(my_handler)

        self.query_logger = q_log

        self.name = "ai"
        self.bot = bot
        self.config = config

    @app_commands.command(name = 'chat')
    async def hello(self, interaction: discord.Interaction, query: str):
        # await interaction.response.send_message('Hello')

        async with aiohttp.ClientSession() as session:
            request_data = {"query": query}
            service_url = createUrl(self.config['model_server']['chat_server'], self.config['model_server']['chat_port'], self.config['model_server']['chat_uri'])

            async with session.post(service_url, data = request_data) as r:
                await interaction.response.defer(ephemeral = True)

                if r.status == 200:
                    js = await r.json()
                    chat_msg = js.get('message', 'Looks like the server sent something weird. Gotta protect your fragile mind from it.')
                    self.query_logger.info(f'Query: {query}, response: {js}')
                    return await interaction.followup.send(chat_msg)
                    # await channel.send(js['file'])
                else:
                    return await interaction.followup.send('Uff kuch to galti hui...')


    @app_commands.command()
    async def dream(self, interaction: discord.Interaction, query: str):
        """tells you what version of the bot software is running."""
        print(f'in dream {query}')
        await interaction.response.send_message('This is not implemented yet')


    @app_commands.command()
    async def execute(self, interaction: discord.Interaction, args: str):
        """Takes different commands. Send help to know more"""
        print(f'args {args}')
        if args == 'help':
            return await interaction.response.send_message('This is an not implemented yet')
        elif args.startswith('dream ') or args == 'dream':
            query = args[5:]
            if not query.strip():
                query = "Something gamey"

            return await self.dream(interaction, query)
        elif args.startswith('chat ') or args == 'chat':
            query = args[4:]
            if not query.strip():
                return await interaction.response.send_message('I need some command hooman!')

            return await self.hello(interaction, query)


        return await interaction.response.send_message('Unknown command use help for list of valid commands')