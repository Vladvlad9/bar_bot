from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def contacts_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Наш адрес"),
                KeyboardButton(text="Номер телефона")
            ],
            [
                KeyboardButton(text="Назад")
            ]
        ]
    )
    return keyboard