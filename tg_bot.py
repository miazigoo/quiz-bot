import logging

from aiogram import Bot, Dispatcher
import asyncio

from aiogram.fsm.storage.memory import MemoryStorage
from environs import Env

from handlers import tg_common, tg_quiz

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    env = Env()
    env.read_env()

    tg_token = env.str("TGTOKEN")
    admin_id = env.str('TELEGRAM_ADMIN_ID')
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=tg_token)
    dp.include_router(tg_common.router)
    dp.include_router(tg_quiz.router)
    logger.info('Telegram bot started')

    await bot.send_message(admin_id, 'Telegram bot started')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
