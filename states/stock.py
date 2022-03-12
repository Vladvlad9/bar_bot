from aiogram.dispatcher.filters.state import StatesGroup, State


class stockST(StatesGroup):
    description = State()
    photo = State()
