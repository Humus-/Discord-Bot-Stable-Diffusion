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