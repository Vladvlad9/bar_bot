from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def menu_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        row_width=3,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Основное меню"),
                KeyboardButton(text="Барное меню"),

            ],
            [
                KeyboardButton(text="Пивная карта"),
                KeyboardButton(text="Пиво в банке")
            ],
            [
                KeyboardButton(text="Назад")
            ]
        ]
    )
    return keyboard