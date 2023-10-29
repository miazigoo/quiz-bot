import logging

from aiogram import Bot, types, Dispatcher, F
import asyncio

from aiogram.filters import Command
from environs import Env


logger = logging.getLogger(__name__)

dp = Dispatcher()


@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message(Command('help'))
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message(F.text)
async def echo_message(msg: types.Message):
    await msg.bot.send_message(msg.from_user.id, msg.text)


async def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    env = Env()
    env.read_env()

    tg_token = env.str("TGTOKEN")
    admin_id = env.str('TELEGRAM_ADMIN_ID')

    bot = Bot(token=tg_token)
    logger.info('Telegram bot started')
    await bot.send_message(admin_id, 'Telegram bot started')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
