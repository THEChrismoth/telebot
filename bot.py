import config
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start(message: types.Message):
    await message.reply("Hello, giv me message!")

if __name__ == '__main__':
    executor.start_polling(dp)
