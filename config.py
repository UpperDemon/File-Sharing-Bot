import os
import logging
from logging.handlers import RotatingFileHandler


# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
if not TG_BOT_TOKEN:
    raise ValueError("TG_BOT_TOKEN environment variable is required.")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))
if APP_ID <= 0:
    raise ValueError("Invalid APP_ID.")

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")
if not API_HASH:
    raise ValueError("API_HASH environment variable is required.")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
if CHANNEL_ID <= 0:
    raise ValueError("Invalid CHANNEL_ID.")

# Start Image
START_IMG = "https://telegra.ph/file/96f14d44c4369420bd9dd.jpg"

# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
if OWNER_ID <= 0:
    raise ValueError("Invalid OWNER_ID.")

# Port
PORT = os.environ.get("PORT", "8080")

# Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Force sub channel id
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in a specified channel and other users can access it from a special link.")

try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split() if x.isdigit()]
    if not ADMINS:
        raise ValueError("Your Admins list does not contain valid integers.")
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me\n\nKindly Please join Channel</b>")

# Set your Custom Caption here
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Prevent users from forwarding files
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"

# Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only a File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)  # Make sure this ID is valid and needed

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
