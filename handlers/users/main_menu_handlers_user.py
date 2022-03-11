from aiogram import types

from keyboards import *
from loader import dp, db


@dp.message_handler(text="Основное меню")
async def load_name(message: types.Message):
    await message.answer("Наше меню", reply_markup= await back_kb())

    markup = types.InlineKeyboardMarkup()
    types.InlineKeyboardMarkup()

    photo = await db.get_photo_main_menu()
    for photo in photo:
        await message.answer_photo(photo[0], reply_markup=markup)


@dp.message_handler(text="Назад")
async def back_main_menu(message: types.Message):
    await message.answer('Главное меню', reply_markup= await start_kb())
