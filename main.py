from aiogram import Bot, Dispatcher, executor, types
import os
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Enable logging
logging.basicConfig(level=logging.INFO)

# Bot token from environment
TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! I'm Gunther Bot. Please follow my YT channel!")

@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo("https://avatars.githubusercontent.com/u/62240649?v=4")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
