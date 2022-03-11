from aiogram import types

from keyboards import *
from loader import dp, db


@dp.message_handler(text=["Основное меню", "Барное меню", "Пивная карта", "Пиво в банке"])
async def load_name(message: types.Message):
    data = {
        'Основное меню': 'main_menu',
        'Барное меню': 'bar_menu',
        'Пивная карта': 'beer_card',
        'Пиво в банке': 'beer_in_can'
    }

    await message.answer("Наше меню", reply_markup= await back_kb())

    markup = types.InlineKeyboardMarkup()
    types.InlineKeyboardMarkup()

    for i, j in data.items():
        if message.text in i:
            photo = await db.get_photo_main_menu(j)
            for photo in photo:
                await message.answer_photo(photo[0], reply_markup=markup)
                break


@dp.message_handler(text="Назад")
async def back_main_menu(message: types.Message):
    await message.answer('Главное меню', reply_markup= await start_kb())
