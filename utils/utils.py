import logging
import yaml
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.DEBUG)

def getLogLevel(level = None):
	if not level:
		level = os.getenv('LOG_LEVEL', default = 'DEBUG')

	if level == 'DEBUG':
		return logging.DEBUG
	elif level == 'INFO':
		return logging.INFO
	elif level == 'WARNING':
		return logging.WARNING
	elif level == 'ERROR':
		return logging.ERROR
	elif level == 'CRITICAL':
		return logging.CRITICAL
	else:
		logger.info(f"Invalid log level {level}")

	return logging.DEBUG

def createUrl(addr, port, resource_uri = None):
	url = ""
	if not addr.startswith("http"):
		url = "http://"

	url += addr + ":" + str(port)

	if resource_uri:
		url += "/" + resource_uri

	return url

def load_config(path):
	config = None
	logger = logging.getLogger(__name__)

	with open(path, "r") as stream:
		try:
			config = yaml.safe_load(stream)

			logger.info("Config Loaded")
		except yaml.YAMLError as exc:
			logger.error("Could not load config file")

	return config
