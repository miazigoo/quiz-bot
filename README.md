## Bot "Quiz"

### Бот для викторин в "Telegram" и "VK"
- Telegram - [@test_python_zeder_bot](https://t.me/test_python_zeder_bot)
- VK - [test bot](https://vk.com/club219710754)


 
### Как установить


* Скачать [этот script](https://github.com/miazigoo/quiz-bot.git)

Перейдите в каталог проекта:
```sh
cd quiz-bot
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.6.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

### Как запустить:

Часть настроек проекта берётся из переменных окружения. 
Чтобы их определить, создайте файл `.env` в каталоге проекта и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступно 6 переменных:

 
- `TELEGRAM_BOT_API_KEY` — Получите токен у [@BotFather](https://t.me/BotFather), вставте в `.env` например: `TELEGRAM_BOT_API_KEY=588535421721:AAFYtrO5YJhpU...`.
- `VK_GROUP_TOKEN` — [token группы VK](https://vk.com/groups?tab=admin), незабудьте в настройках группы включить сообщения.
- `QUESTIONS_FOLDER` — Путь до папки с файлами-вопросами
- `REDIS_HOST`, `REDIS_PORT`: Параметры для соединения с  redis db
- `TELEGRAM_ADMIN_ID` — ваш телеграм id. получить его можно у [@userinfobot ](https://t.me/userinfobot), отправив любое сообщение.

# Start

```sh
python tg_bot.py # Telegram-bot
python vk_bot.py # VK - bot
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
