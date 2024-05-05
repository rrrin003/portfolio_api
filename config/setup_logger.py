import logging

from apscheduler.schedulers.background import BackgroundScheduler

from common import common
from common import constants

today = common.get_datetime_str("%Y-%m-%d")

log_level = logging.INFO
log_format = "【%(asctime)s】 <%(levelname)s> %(module)s.py : %(lineno)d - %(message)s"

log_file_name = today + ".log"
log_file_path = "log/" + log_file_name


def generate_log_file():
    """ログファイル生成

    空のログファイルを作成
    """

    f = open(log_file_path, "w")
    f.write("")
    f.close()


def setup_logger():
    """ロガーセットアップ関数"""

    generate_log_file()

    logger = logging.getLogger(constants.API_LOGGER)
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(log_file_path, mode="a")
    file_handler.setFormatter(formatter)
    logger.setLevel(log_level)
    logger.addHandler(file_handler)


def setup_logger_periodic_execution():
    """setup_loggerを毎日00:00に実行"""

    setup_logger()

    scheduler = BackgroundScheduler()
    scheduler.add_job(setup_logger, "cron", hour=00, minute=00)
    scheduler.start()
