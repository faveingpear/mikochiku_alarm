import os
from os.path import join, dirname
import dotenv #Was getting import errors from pyinstaller not including dotenv because it was in the format 'from dotenv import load_dotenv' 

dotenv.load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

CHID = os.environ.get("CHANNEL_ID")
ICON = os.environ.get("ICON_PATH")
ALARM = os.environ.get("ALARM_PATH")
LOG_DIR = os.environ.get("LOG_DIR")
LOG_NAME = os.environ.get("LOG_NAME")
