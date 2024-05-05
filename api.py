import logging

from fastapi import FastAPI

from common import constants
from config.setup_logger import setup_logger_periodic_execution

app = FastAPI()

setup_logger_periodic_execution()

logger = logging.getLogger(constants.API_LOGGER)

logger.info("test")
