import yaml
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

CONFIG_PATH = "./discord_src/utils/config.yml"

class Config:
  __conf = None
  __setters = []

  @staticmethod
  def load_config(path : str = CONFIG_PATH) -> None:
    """Loads the config from the path file. This is a yml file that has some access info about the different services."""
    with open(path, "r") as stream:
      try:
        Config.__conf = yaml.safe_load(stream)

        logger.info("Config Loaded")
      except yaml.YAMLError as exc:
        logger.error("Could not load config file")

  @staticmethod
  def get(key: str) -> any:
    """Get the requested key from the config obj and send it back."""

    # load the config from the file if not already done.
    if not Config.__conf:
      Config.load_config(CONFIG_PATH)

    if key not in Config.__conf:
      return KeyError(f'Key: {{key}} not found')

    print(f'config obj: {Config.__conf}')

    return Config.__conf[key]

  @staticmethod
  def set(key: str, val: any) -> None:
    """
    Set the config value if that is one of the mutable paths.
    """

    # load the config from the file if not already done.
    if not Config.__conf:
      Config.load_config(CONFIG_PATH)

    if key in Config.__setters:
      Config.__conf[key] = val
    else:
      raise NameError('Not allowed to edit this value')