import logging

import vk_api
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

from handlers.vk_quiz import handle_new_question, handle_give_up, handle_solution_attempt, handle_my_account
from load_quiz import load_books
from redis_connection import get_redis_connection

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    env = Env()
    env.read_env()

    vk_api_key = env.str("VK_API_KEY")
    vk_session = vk_api.VkApi(token=vk_api_key)

    api_vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    redis_connect = get_redis_connection()
    books = load_books()

    for event in longpoll.listen():
        if not (event.type == VkEventType.MESSAGE_NEW and event.to_me):
            continue

        if event.text == 'Новый вопрос':
            handle_new_question(event, api_vk, redis_connect, books)
            continue

        if event.text == 'Сдаться':
            handle_give_up(event, api_vk, redis_connect)
            continue

        if event.text == 'Мой счет':
            handle_my_account(event, api_vk, redis_connect)
            continue

        handle_solution_attempt(event, api_vk, redis_connect)


if __name__ == "__main__":
    main()
