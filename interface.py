import logging
import apikeys
import emoji
import MessageConstructor

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

# настройки бота (замените их своими данными)
BOT_TOKEN = apikeys.TelegramBotApiKeys.API_KEY_DEV
CHAT_ID = "710621392"

# настройки логирования
logging.basicConfig(level=logging.INFO)

# создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# определяем состояния
class UserState(StatesGroup):
    REQUEST_WEATHER = State()
    FEEDBACK = State()

# обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Запросить погоду", "Обратная связь"]
    keyboard.add(*buttons)

    start_message = f"Привет {emoji.emojize(':wave:')}! Я Useful Forecast Bot {emoji.emojize(':sun_behind_small_cloud:')} и я помогу тебе узнавать о погоде в любой точке мира {emoji.emojize(':earth_africa:')}. Просто напиши мне название города, и я пришлю тебе актуальную информацию о температуре, влажности, скорости ветра, атмосферном давлении и прогноз на ближайшие дни {emoji.emojize(':calendar:')}. Кроме того, я могу дать персонализированные рекомендации на основе погодных условий, такие как подходящая одежда и активности, чтобы помочь тебе подготовиться к дню вперед {emoji.emojize(':watch:')}. Давай начнем!"
    await message.answer(
        start_message,
        reply_markup=keyboard,
        disable_notification=True,
        disable_web_page_preview=True
    )


# обработчик для кнопки "Запросить погоду"
@dp.message_handler(Text(equals="Запросить погоду"))
async def request_weather(message: types.Message):
    await message.answer(MessageConstructor.ForecastMessageConstructor.getCurrentWeatherMessage())

# обработчик для кнопки "Обратная связь"
@dp.message_handler(Text(equals="Обратная связь"))
async def feedback(message: types.Message):
    await message.answer("Напиши свой вопрос или предложение.")
    await UserState.FEEDBACK.set()

# обработчик для получения города
@dp.message_handler(state=UserState.REQUEST_WEATHER)
async def process_weather_city(message: types.Message, state: FSMContext):
    city = message.text
    await state.finish()

    await message.answer(MessageConstructor.ForecastMessageConstructor.getCurrentWeatherMessage())

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
