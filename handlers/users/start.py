from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import start_kb
from keyboards.default.admin import adminKB
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup= await start_kb())
    referral = message.get_args()


    if referral:
        balance = await db.check_balance(referral)
        new_balance = balance[0]
        result_balance = new_balance[0] + 5
        await db.add_new_user_referral(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                                       referral)
        await db.add_money_user(result_balance, referral)

    if not await db.select_user(message.from_user.id):
        await db.add_new_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name)



    print('asd')


@dp.message_handler(commands=["create_database", "create_db", ])
async def create_database(message: types.Message):
    await message.answer(text="База данных успешно создана!")
    await db.create_all_database()


@dp.message_handler(commands=["moderator", "admin", ])
async def create_database(message: types.Message):
    await message.answer(text="Вы вошли как админ", reply_markup=await adminKB.start_kb_admin())