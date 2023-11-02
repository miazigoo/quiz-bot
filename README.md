## Bot "Quiz"

### Бот для викторин в "Telegram" и "VK"


 
### Как установить


* Скачать [этот script](https://github.com/miazigoo/quiz-bot.git)

**Python3 уже должен быть установлен**. 
Используйте `pip` (или `pip3`, если возникает конфликт с Python2) для установки зависимостей:
```sh
pip install -r requirements.txt
```

### Как запустить:

Часть настроек проекта берётся из переменных окружения. 
Чтобы их определить, создайте файл `.env` в каталоге проекта и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступно 5 переменных:

 
- `TELEGRAM_BOT_API_KEY` — Получите токен у [@BotFather](https://t.me/BotFather), вставте в `.env` например: `TELEGRAM_BOT_API_KEY=588535421721:AAFYtrO5YJhpU...`.
- `VK_GROUP_TOKEN` — [token группы VK](https://vk.com/groups?tab=admin), незабудьте в настройках группы включить сообщения.
- `QUESTIONS_FOLDER` — Путь до папки с файлами-вопросами
- `REDIS_HOST`, `REDIS_PORT`: Параметры для соединения с  redis db

# Start

```sh
python tg_bot.py # Telegram-bot
python vk_bot.py # VK - bot
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
