from dataclasses import dataclass
from typing import Optional

from marshmallow_dataclass import class_schema

from droid import config_factory
from droid.logs import LoggingConfig


@dataclass
class ModelConf:
    threshold: float
    model_path: Optional[str] = None


@dataclass
class SmartConf:
    name: str
    logging: LoggingConfig
    model: ModelConf


SmartConfSchema = class_schema(SmartConf)

conf: SmartConf = SmartConfSchema().load(config_factory(folder='settings'))
