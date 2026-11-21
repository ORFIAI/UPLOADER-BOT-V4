import logging
import os
from os import environ


def _required_env(name):
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            "Add it in your hosting provider's Environment settings."
        )
    return value


def _int_env(name, default=None, required=False):
    value = os.environ.get(name, "").strip()
    if not value:
        if required:
            raise RuntimeError(
                f"Missing required environment variable: {name}. "
                "Add it in your hosting provider's Environment settings."
            )
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable {name} must be an integer.") from exc


logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)


class Config(object):
    BOT_TOKEN = _required_env("BOT_TOKEN")
    API_ID = _int_env("API_ID", required=True)
    API_HASH = _required_env("API_HASH")

    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 2194304000
    TG_MAX_FILE_SIZE = 2194304000
    FREE_USER_MAX_FILE_SIZE = 2194304000
    CHUNK_SIZE = _int_env("CHUNK_SIZE", 128)
    DEF_THUMB_NAIL_VID_S = os.environ.get(
        "DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90"
    )
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    DEF_WATER_MARK_FILE = "@UploaderXNTBot"

    ADMIN = {
        int(x) for x in environ.get("ADMIN", "").split() if x.isdigit()
    }
    BANNED_USERS = {
        int(x) for x in environ.get("BANNED_USERS", "").split() if x.isdigit()
    }

    DATABASE_URL = _required_env("DATABASE_URL")
    LOG_CHANNEL = _int_env("LOG_CHANNEL", 0)
    LOGGER = logging
    OWNER_ID = _int_env("OWNER_ID", required=True)
    SESSION_NAME = "UploaderXNTBot"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "").strip()

    TG_MIN_FILE_SIZE = 2194304000
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "").strip()
    ADL_BOT_RQ = {}

    TRUE_OR_FALSE = os.environ.get("TRUE_OR_FALSE", "").lower() == "true"

    SHORT_DOMAIN = environ.get("SHORT_DOMAIN", "")
    SHORT_API = environ.get("SHORT_API", "")
    VERIFICATION = os.environ.get("VERIFICATION", "")
