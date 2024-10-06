import logging
from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # You can change this to logging.DEBUG for more details
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    try:
        now = datetime.now()
        delta = now - bot.uptime
        time = get_readable_time(delta.seconds)
        await message.reply(BOT_STATS_TEXT.format(uptime=time))
        logger.info(f"Stats command used by {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in /stats command: {e}", exc_info=True)
        await message.reply("An error occurred while processing the command.")


@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    try:
        # Only send reply to non-admin users
        if message.from_user.id not in ADMINS:
            if USER_REPLY_TEXT:
                await message.reply(USER_REPLY_TEXT)
                logger.info(f"Sent USER_REPLY_TEXT to {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in useless handler: {e}", exc_info=True)
        await message.reply("An error occurred.")
