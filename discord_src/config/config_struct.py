import dataclasses
from typing import Optional

# Pydantic has more validation features, plus it gives us static and runtime type safety.
from pydantic import Field
from pydantic.dataclasses import dataclass

import hydra  # other option was to use the bison package
from hydra.core.config_store import ConfigStore

@dataclass
class ModelServerParams:
  sd_server: str
  sd_port: int
  sd_uri: str
  chat_server: str
  chat_port: int
  chat_uri: str

@dataclass
class Paths:
  data_path: str
  log_path: Optional[str] = Field('./logs', title='The folder where log are stored')

@dataclass
class AppConfig:
  open_ai_fallback: bool
  model_params: ModelServerParams = dataclasses.field(default_factory = ModelServerParams)
  proj_paths: Paths = dataclasses.field(default_factory = Paths)


cs = ConfigStore.instance()
cs.store(name = 'app_config', node = AppConfig)
