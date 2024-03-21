import os
import telegram
import asyncio

# Get the bot token and chat ID from environment variables or config file
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

def send_alert(message):
    asyncio.run(send(message)) 

async def send(message):
    print(message)
    if bot_token is not None and chat_id is not None:
        bot = telegram.Bot(token=bot_token)
        await bot.sendMessage(chat_id=chat_id, text=message)