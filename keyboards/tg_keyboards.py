from aiogram import types


start_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Новый вопрос"),
            types.KeyboardButton(text="Сдаться")
        ],
        [types.KeyboardButton(text="Мой счет")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите"
)
