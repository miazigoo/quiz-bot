import random

from vk_api.utils import get_random_id

from keyboards.vk_keyboards import get_start_keyboard


def handle_new_question(event, vk, redis_connect, books):
    """
    Выдает случайный вопрос
    """
    book_row = random.choice(random.choice(books))
    redis_connect.set(event.user_id, book_row["answer"].encode('koi8-r'))
    vk.messages.send(
        peer_id=event.user_id,
        random_id=get_random_id(),
        keyboard=get_start_keyboard(),
        message=book_row['question']
    )


def handle_solution_attempt(event, vk, redis_connect):
    """
    Проверка на правильность ответа
    """
    user_id = event.user_id
    answer = redis_connect.get(event.user_id)
    point = redis_connect.get(f'point_{user_id}')
    if not point:
        redis_connect.set(f'point_{user_id}', 0)
    if answer:
        if event.text in answer.decode('koi8-r').lower():
            point = 1 + int(point.decode("koi8-r")) if point else 0
            redis_connect.set(f'point_{user_id}', point)
            vk.messages.send(
                peer_id=event.user_id,
                random_id=get_random_id(),
                keyboard=get_start_keyboard(),
                message=f'Правильно! Поздравляю! Для следующего вопроса нажмите «Новый вопрос».'
            )
        else:
            vk.messages.send(
                peer_id=event.user_id,
                random_id=get_random_id(),
                keyboard=get_start_keyboard(),
                message='Неправильно. Попробуйте ещё раз.'
            )
    else:
        message = (
            'Не был задан вопрос или нет на него ответа. \n'
            'Чтобы продолжить нажмите «Новый вопрос».'
        )
        vk.messages.send(
            peer_id=event.user_id,
            random_id=get_random_id(),
            keyboard=get_start_keyboard(),
            message=message
        )


def handle_give_up(event, vk, redis_connect):
    """
    Показывает ответ.
    """
    user_id = event.user_id
    answer = redis_connect.get(event.user_id)
    give_up = redis_connect.get(f"give_up_{user_id}")
    if not give_up:
        redis_connect.set(f'give_up_{user_id}', 0)
    if answer:
        give_up = 1 + int(give_up.decode("koi8-r")) if give_up else 0
        redis_connect.set(f"give_up_{user_id}", give_up)
        message = (
            f'Ответ был: {answer.decode("koi8-r")}\n'
            'Чтобы продолжить нажмите «Новый вопрос».'
        )
        vk.messages.send(
            peer_id=event.user_id,
            random_id=get_random_id(),
            keyboard=get_start_keyboard(),
            message=message
        )
    else:
        message = (
            'Не был задан вопрос или нет на него ответа. \n'
            'Чтобы продолжить нажмите «Новый вопрос».'
        )
        vk.messages.send(
            peer_id=event.user_id,
            random_id=get_random_id(),
            keyboard=get_start_keyboard(),
            message=message
        )


def handle_my_account(event, vk, redis_connect):
    """
    Показывает счет
    """
    user_id = event.user_id
    point = redis_connect.get(f"point_{user_id}")
    give_up = redis_connect.get(f"give_up_{user_id}")
    answer = (f'Вы ответили верно на: {point.decode("koi8-r") if point else 0} вопрос(а/ов)\n'
              f'Вы сдались: {give_up.decode("koi8-r") if give_up else 0} раз')
    vk.messages.send(
        peer_id=event.user_id,
        random_id=get_random_id(),
        keyboard=get_start_keyboard(),
        message=answer
    )

