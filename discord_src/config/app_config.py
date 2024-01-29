import dataclasses
from typing import Optional

# Pydantic has more validation features, plus it gives us static and runtime type safety.
from pydantic import Field
from pydantic.dataclasses import dataclass

from omegaconf import MISSING

import hydra  # other option was to use the bison package
from hydra.core.config_store import ConfigStore

@dataclass
class ModelServerParams:
  sd_server: str = MISSING
  sd_port: int = MISSING
  sd_uri: str = MISSING
  chat_server: str = MISSING
  chat_port: int = MISSING
  chat_uri: str = MISSING

@dataclass
class Paths:
  data_path: str = './data'
  log_path: Optional[str] = Field('./logs', title='The folder where log are stored')

@dataclass
class AppConfig:
  open_ai_fallback: bool
  model_params: ModelServerParams = dataclasses.field(default_factory = ModelServerParams)
  proj_paths: Paths = dataclasses.field(default_factory = Paths)


cs = ConfigStore.instance()
cs.store(name = 'app_config', node = AppConfig)
# cs.store(name="config2", node=MySQLConfig(host="test.db", port=3307))