from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        row_width=3,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Основное меню"),
                KeyboardButton(text="Барное меню"),
                KeyboardButton(text="Пивная карта")
            ],
            [
                KeyboardButton(text="Пиво в банке"),
                KeyboardButton(text="Футбольные трансляции"),
                KeyboardButton(text="Акции")
            ],
            [
                KeyboardButton(text="Забронировать столик"),
                KeyboardButton(text="Оставить отзыв"),
                KeyboardButton(text="Программа лояльности")
            ],
            [
                KeyboardButton(text="Наши заведения")
            ]
        ]
    )
    return keyboard