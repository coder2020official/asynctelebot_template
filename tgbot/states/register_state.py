# Create your states in this folder.


from telebot.asyncio_handler_backends import State, StatesGroup


class Register(StatesGroup):
    """
    Group of states for registering
    """
    name = State()
    surname = State()