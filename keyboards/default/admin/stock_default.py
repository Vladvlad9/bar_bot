from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


async def stock_Df_admin():
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text='Да'),
                KeyboardButton(text='Нет'),
            ]
        ]
    )
    return keyboard