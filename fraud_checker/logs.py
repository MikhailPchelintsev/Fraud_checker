from logging import Logger

from droid.logs import setup_logging
from fraud_checker.config.config import conf


def initialize_logs() -> Logger:
    return setup_logging(
        app_name=conf.name,
        app_level=conf.logging.level,
        log_format=conf.logging.formatting,
        loggers=conf.logging.loggers,
    )
