# intention is to make this a cli launcher to launch either the app or the server using the same application

import logging
import os
from dotenv import load_dotenv
from threading import Thread

from utils import utils

from discord_src.bot import discord_bot#, image_client


#### INIT CODE HERE
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CONFIG_PATH = "utils/config.yml"

config = None

# Logger
logging.basicConfig(level=logging.INFO,
					filename = "./logs/py_log.log",
					filemode = "w",
					format = "%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info('Initing config')

config = utils.load_config(CONFIG_PATH)

####INIT ENDS


logger.info('Launching bot')

# os.environ["CUDasdfasf"] = "1"


def main():
	# TODO: Check and launch the Flask application

	# discord_client = discord_bot.create_discord_client(config)
	# discord_client.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
	main()