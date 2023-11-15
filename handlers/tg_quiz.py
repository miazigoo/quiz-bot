import random

from aiogram import F, Router, types
from aiogram.types import Message

from keyboards.tg_keyboards import start_keyboard

router = Router()


def get_random_question_and_set_answer(user_id, redis_connect, books):
    book_row = random.choice(random.choice(books))
    redis_connect.set(user_id, book_row["answer"].encode('koi8-r'))
    return book_row["question"]


@router.message(F.text.lower() == 'новый вопрос')
async def handle_new_question_request(message: Message, redis_connect: object, books: list):
    """
    Выдает случайный вопрос
    """
    question = get_random_question_and_set_answer(message.from_user.id, redis_connect, books)
    await message.answer(question, reply_markup=start_keyboard)


@router.message(F.text.lower() == 'сдаться')
async def handle_give_up(message: Message, redis_connect: object, books: list):
    """
    Показывает ответ. Выдает новый случайный вопрос
    """
    user_id = message.from_user.id
    answer = redis_connect.get(user_id)
    give_up = redis_connect.get(f"give_up_{user_id}")
    if answer:
        give_up = 1 + int(give_up.decode("koi8-r")) if give_up else 0
        redis_connect.set(f"give_up_{user_id}", give_up)
        await message.answer(f'Ответ на вопрос был:\n{answer.decode("koi8-r")}\n')
        await handle_new_question_request(message, redis_connect, books)
    else:
        await message.answer('Для справки наберите /help', reply_markup=start_keyboard)


@router.message(F.text.lower() == 'мой счет')
async def handle_my_account(message: Message, redis_connect: object):
    """
    Показывает счет
    """
    user_id = message.from_user.id
    point = redis_connect.get(f"point_{user_id}")
    give_up = redis_connect.get(f"give_up_{user_id}")
    answer = (f'Вы ответили верно на: {point.decode("koi8-r") if point else 0} вопрос(а/ов)\n'
              f'Вы сдались: {give_up.decode("koi8-r") if give_up else 0} раз')
    await message.answer(answer, reply_markup=start_keyboard)


@router.message(F.text)
async def handle_solution_attempt(message: types.Message, redis_connect: object):
    """
    Проверка на правильность ответа
    """
    msg = message.text.lower()
    user_id = message.from_user.id
    answer = redis_connect.get(user_id)
    point = redis_connect.get(f'point_{user_id}')
    if not point:
        redis_connect.set(f'point_{user_id}', 0)
    if answer:
        if msg in answer.decode('koi8-r').lower():
            point = 1 + int(point.decode("koi8-r")) if point else 0
            redis_connect.set(f'point_{user_id}', point)
            redis_connect.delete(user_id)
            await message.answer('Поздравляю! Вы ответили правильно! \n'
                                 f'Ответ: «{answer.decode("koi8-r")}»\n'
                                 'Для следующего вопроса нажмите кнопку «Новый вопрос».',
                                 reply_markup=start_keyboard)
        else:
            await message.answer('К сожалению, вы ответили неправильно. Попробуйте еще раз.',
                                 reply_markup=start_keyboard)
    else:
        await message.answer('К сожалению, не понимаю вас. Для справки наберите /help',
                             reply_markup=start_keyboard)
