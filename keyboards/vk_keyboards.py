from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_start_keyboard():
    keyboard = VkKeyboard()
    keyboard.add_button('Новый вопрос', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Сдаться', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Мой счет', color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()
