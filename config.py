import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6687996041:AAHUix_UdDeeiJahiWyzS59K7KRc95U1hdI")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "2354655"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "1710ccf07d51d7c8e66a095d089461d2")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
