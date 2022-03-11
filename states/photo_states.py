from aiogram.dispatcher.filters.state import StatesGroup, State


class main_menu_state(StatesGroup):
    name_message_handler = State()
    photo = State()
