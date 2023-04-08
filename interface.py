import logging
import api_keys
import message_constructor
import requests

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Location, Message
from aiogram.utils import executor

# настройки бота (замените их своими данными)
BOT_TOKEN = api_keys.TelegramBotApiKeys.API_KEY_DEV
CHAT_ID = api_keys.TelegramBotApiKeys.CHAT_ID

# настройки логирования
logging.basicConfig(level=logging.INFO)

# создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# определяем состояния


class UserState(StatesGroup):
    REQUEST_WEATHER = State()
    FEEDBACK = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    # Запрашиваем геолокацию
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_location = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_location)
    await message.reply("Пожалуйста, отправьте мне свое местоположение, чтобы я мог предоставить вам прогноз погоды для вашего города.", reply_markup=keyboard)


@dp.message_handler(content_types=['location'])
async def process_location(message: Message):
    # Получаем координаты пользователя
    latitude = message.location.latitude
    longitude = message.location.longitude

    # Получаем название города по координатам
    url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={latitude}&lon={longitude}&limit=1&appid={'05e84bfef4dccd07dfc410a0b26c8cc9'}"
    response = requests.get(url)
    json_data = response.json()
    city_name = json_data[0]['name']
    await message.reply(f"Спасибо, ваше местоположение: {city_name}.")

    # Получаем текущий прогноз погоды
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.environ['OPENWEATHERMAP_API_KEY']}&units=metric&lang=ru"
    response = requests.get(url)
    json_data = response.json()
    weather_description = json_data['weather'][0]['description']
    temperature = json_data['main']['temp']
    await message.reply(f"Сейчас в городе {city_name} {weather_description}, температура: {temperature} °C.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# обработчик для кнопки "Обратная связь"


@dp.message_handler(Text(equals="Обратная связь"))
async def feedback(message: types.Message):
    await message.answer("Напиши свой вопрос или предложение.")
    await UserState.FEEDBACK.set()

# обработчик для получения обратной связи


@dp.message_handler(state=UserState.FEEDBACK)
async def process_feedback(message: types.Message, state: FSMContext):
    feedback_text = message.text
    await state.finish()

    await message.answer("Спасибо за обратную связь!")

    # отправляем обратную связь на ваш чат в телеграме
    await bot.send_message(CHAT_ID, f"Новая обратная связь: {feedback_text}")

# запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
