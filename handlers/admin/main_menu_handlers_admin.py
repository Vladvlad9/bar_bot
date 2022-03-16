from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default import main_menu_admin
from keyboards.inline.admin import edit_inline_keyboard
from loader import dp, db
from states import main_menu_state

data ={
        'Основное меню_admin': 'main_menu',
        'Барное меню_admin': 'bar_menu',
        'Пивная карта_admin': 'beer_card',
        'Пиво в банке_admin': 'beer_in_can'
    }


@dp.message_handler(state='*', commands="Назад_")
@dp.message_handler(Text(equals='Назад_', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_data()

    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


@dp.message_handler(text=["Основное меню_admin", "Барное меню_admin", "Пивная карта_admin", "Пиво в банке_admin"])
async def load_name(message: types.Message, state: FSMContext):
    await message.answer("Произведите действия", reply_markup= await main_menu_admin())
    await state.update_data(name_handlers=message.text)


@dp.message_handler(text="Добавить", state=None)
async def cm_start(message: types.Message):
    await main_menu_state.photo.set()
    await message.reply('Загрузить фото')


@dp.message_handler(content_types=['photo'], state=main_menu_state.photo)
async def load_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    data_state = await state.get_data()

    photo = data_state['photo']
    name_BD = data_state['name_handlers']

    for name_handler, name_bd in data.items():
        if name_BD in name_handler:
            if await db.add_new_photo_main_menu(photo, name_bd):
                await message.answer('Вы успешно загрузили изображение')
            break

    await state.finish()


@dp.message_handler(text=["Редактировать"])
async def load_name(message: types.Message, state: FSMContext):
    data_state = await state.get_data()
    name_BD = data_state['name_handlers']

    for _name_handler, _name_bd in data.items():
        if name_BD in _name_handler:
            photo = await db.get_photo_main_menu(_name_bd)

    for i in photo:
        await message.answer_photo(i[1], reply_markup=await edit_inline_keyboard(i[0]))
        break


@dp.callback_query_handler(lambda call: "delete_" in call.data)
async def update_menu(call: types.CallbackQuery, state: FSMContext):
    id_photo_bd = call.data.split('_')
    id_photo = id_photo_bd[1]

    data_state = await state.get_data()
    name_BD = data_state['name_handlers']

    for _name_handler, _name_bd in data.items():
        if name_BD in _name_handler:
            delete_photo = await db.delete_photo_main_menu(_name_bd, id_photo_bd[1])

    if delete_photo:
        await call.message.answer('Вы успешно удалили изображение')