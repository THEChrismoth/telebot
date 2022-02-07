import config
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, чтобы узнать список команд напиши /help")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/start-запуск бота и вывод стартового сообщения \n"
                        "/help-список комманд бота \n"
                        "/graphics-сыылки на видеокарты Aliexpress")

@dp.message_handler(commands=['gpraphics'])
async def process_graphics_command(message: types.Message):
    await message.reply("")


if __name__ == '__main__':
    executor.start_polling(dp)
