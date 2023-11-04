import logging
from dotenv import load_dotenv

load_dotenv()

def getLogLevel(level = None):
	if not level:
		level = os.getenv('LOG_LEVEL', default = 'DEBUG')
	
	if level == 'DEBUG':
		return logging.DEBUG
	if level == 'INFO':
		return logging.INFO
	if level == 'WARNING':
		return logging.WARNING
	if level == 'ERROR':
		return logging.ERROR
	if level == 'CRITICAL':
		return logging.CRITICAL

	logging.basicConfig()
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)

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