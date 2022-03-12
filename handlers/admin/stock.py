from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import stock_Df_admin
from keyboards.inline.admin import stock_inline_keyboard
from states import stockST

from loader import dp, db


@dp.message_handler(text="Акции_admin")
async def stock_name(message: types.Message):
    await message.answer("Введите описание акции")
    await stockST.description.set()


@dp.message_handler(state=stockST.description)
async def description_stock(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await stockST.next()
    await stockST.photo.set()
    await message.answer("Загрузить изображение")


@dp.message_handler(content_types=['photo'], state=stockST.photo)
async def description_adds_stock(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    data_state = await state.get_data()

    photo = data_state['photo']
    description = data_state['description']

    if await db.add_stock(photo, description):
        await message.answer('Вы успешно добавили акцию')
    await state.finish()




