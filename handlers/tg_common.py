from aiogram import F, Router, types
from aiogram.filters import Command

from keyboards.tg_keyboards import start_keyboard

router = Router()


@router.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nЯ бот для викторин!",
                         reply_markup=start_keyboard)


@router.message(Command('help'))
async def process_help_command(message: types.Message):
    await message.reply("Бот для викторин, чтобы начать, нажмите: Новый вопрос",
                        reply_markup=start_keyboard)
