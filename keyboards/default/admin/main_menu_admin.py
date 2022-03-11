from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


async def main_menu_admin():
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text='Основное меню Добавить'),
                KeyboardButton(text='Основное меню Изменить'),
                KeyboardButton(text='Основное меню Удалить'),
            ],
            [
                KeyboardButton(text='Назад'),
            ]
        ]
    )
    return keyboard