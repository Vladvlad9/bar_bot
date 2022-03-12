from aiogram.dispatcher.filters.state import StatesGroup, State


class bookingST(StatesGroup):
    fname_user = State()
    lname_user = State()
    date = State()
    time = State()
    number_people = State()
