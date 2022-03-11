from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import main_menu_admin
from loader import dp, db
from states import main_menu_state


@dp.message_handler(text=["Основное меню_admin", "Барное меню_admin", "Пивная карта_admin", "Пиво в банке_admin"])
async def load_name(message: types.Message, state: FSMContext):
    await message.answer("Произведите действия", reply_markup= await main_menu_admin())
    await state.update_data(name_handlers=message.text)
    print('a')

@dp.message_handler(text="Добавить", state=None)
async def cm_start(message: types.Message):

    await main_menu_state.photo.set()
    await message.reply('Загрузить фото')


@dp.message_handler(content_types=['photo'], state=main_menu_state.photo)
async def load_photo(message: types.Message, state: FSMContext):
    data ={
        'Основное меню_admin': 'main_menu',
        'Барное меню_admin': 'bar_menu',
        'Пивная карта_admin': 'beer_card',
        'Пиво в банке_admin': 'beer_in_can'
    }

    await state.update_data(photo=message.photo[0].file_id)
    data_state = await state.get_data()

    photo = data_state['photo']
    name_BD = data_state['name_handlers']

    for name_handler, name_bd in data.items():
        if name_BD in name_handler:
            await db.add_new_photo_main_menu(photo, name_bd)
            break

    await state.finish()