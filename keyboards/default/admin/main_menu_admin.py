from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


async def main_menu_admin():
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text='Добавить'),
                KeyboardButton(text='Изменить'),
                KeyboardButton(text='Удалить'),
            ],
            [
                KeyboardButton(text='Назад'),
            ]
        ]
    )
    return keyboard