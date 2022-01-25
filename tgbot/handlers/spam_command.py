from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message


async def anti_spam(message: Message, bot: AsyncTeleBot):
    """
    You can create a function and use parameter pass_bot.
    """

    await bot.send_message(
        message.chat.id,
        """This is demo spam command.
If you send this command more than once within 2 seconds, 
bot will warn you.
This is made by using middlewares."""
)