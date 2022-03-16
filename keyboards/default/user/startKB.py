from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def back_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Назад")
            ]
        ]
    )
    return keyboard


async def back_kb_mn() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Назад")
            ]
        ]
    )
    return keyboard


async def start_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        row_width=3,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Меню")
            ],
            [

                KeyboardButton(text="Футбольные трансляции"),
                KeyboardButton(text="Акции"),
                KeyboardButton(text="Забронировать столик"),
            ],
            [
                KeyboardButton(text="Контакты"),
                KeyboardButton(text="Оставить отзыв"),
                KeyboardButton(text="Программа лояльности")
            ],
            [
                KeyboardButton(text="Наши заведения")
            ]
        ]
    )
    return keyboard

async def start_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        row_width=3,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Меню")
            ],
            [

                KeyboardButton(text="Футбольные трансляции"),
                KeyboardButton(text="Акции"),
                KeyboardButton(text="Забронировать столик"),
            ],
            [
                KeyboardButton(text="Контакты"),
                KeyboardButton(text="Оставить отзыв"),
                KeyboardButton(text="Программа лояльности")
            ],
            [
                KeyboardButton(text="Наши заведения")
            ]
        ]
    )
    return keyboard