from aiogram.dispatcher.filters.state import StatesGroup, State


class reviewST(StatesGroup):
    grade = State()
    description = State()
