import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from BOT_TOKEN import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN = BOT_TOKEN

dp = Dispatcher

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! i`m oriole bot. Can i halp you?")

async def main():
    await dp.start_polling(Bot)

if __name__ == "__main__":
    asyncio.run(main())