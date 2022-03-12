from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



async def start_kb_admin():
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text='Основное меню_admin'),
                KeyboardButton(text='Барное меню_admin')
            ],
            [
                KeyboardButton(text='Пивная карта_admin'),
                KeyboardButton(text='Пиво в банке_admin')
            ],
            [
                KeyboardButton(text='Акции_admin')
            ]
        ]
    )
    return keyboard