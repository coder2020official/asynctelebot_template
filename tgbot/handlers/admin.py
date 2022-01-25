from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

async def admin_user(message: Message, bot: AsyncTeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    await bot.send_message(message.chat.id, "Hello, admin!")