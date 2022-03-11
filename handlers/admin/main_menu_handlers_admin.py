from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import main_menu_admin
from loader import dp, db
from states import main_menu_state


@dp.message_handler(text="Основное меню_admin")
async def load_name(message: types.Message):
    await message.answer("Произведите действия", reply_markup= await main_menu_admin())


@dp.message_handler(text="Основное меню Добавить", state=None)
async def cm_start(message: types.Message):
    await main_menu_state.photo.set()
    await message.reply('Загрузить фото')


@dp.message_handler(content_types=['photo'], state=main_menu_state.photo)
async def load_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    photo = await state.get_data()

    await db.add_new_photo_main_menu(photo)

    await state.finish()