# intention is to make this a cli launcher to launch either the app or the server using the same application

import logging
import os
from dotenv import load_dotenv
from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
	print('App running')

def run():
	app.run(host = '0.0.0.0', port = 8080)


def launch_app():
	t = Thread(target = run)
	t.start()

load_dotenv()

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info("This is an info message")