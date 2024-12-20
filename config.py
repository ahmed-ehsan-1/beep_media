import logging
import os

DEBUG = os.getenv("DEBUG_MODE", "True").lower() == "true"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "")
HOST = os.getenv("APPLICATION_HOST", "127.0.0.1")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))

VIMEO_CLIENT_ID = os.getenv("VIMEO_CLIENT_ID", "")
VIMEO_CLIENT_SECRET = os.getenv("VIMEO_CLIENT_SECRET", "")
VIMEO_ACCESS_TOKEN = os.getenv("VIMEO_ACCESS_TOKEN", "")

WISTIA_API_TOKEN = os.getenv("WISTIA_API_TOKEN", "")

SURVEY_MONKEY_CLIENT_SECRET= os.getenv("SURVEY_MONKEY_CLIENT_SECRET", "")
SURVEY_MONKEY_CLIENT_ID = os.getenv("SURVEY_MONKEY_CLIENT_ID", "")
SURVEY_MONKEY_REDIRECT_URI = os.getenv("SURVEY_MONKEY_REDIRECT_URI", "")
SURVEY_MONKEY_ACCESS_TOKEN = os.getenv("SURVEY_MONKEY_ACCESS_TOKEN", "")

logging.basicConfig(
    filename=os.getenv("APP_LOG", "app.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
