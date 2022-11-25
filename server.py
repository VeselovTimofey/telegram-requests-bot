"""Telegram bot server, run from this file"""
import logging
import os
import time

from aiogram import Bot, Dispatcher, types

import appeal

log_name = f"{time.strftime('%Y-%m-%d %H.%M', time.localtime())}.log"
logging.basicConfig(level=logging.INFO, filename=log_name)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    """Send help on bot commands"""
    await message.answer(
        "Бот для отправления заявки на возврат товара\n"
        "Просмотреть все свои заявления: /appeals\n"
        "Отправить заявления: /create_appel\n"
    )


@dp.message_handler(commands=["appels"])
async def appeals(message: types.Message):
    """Send all user appeals"""
    user_id = message.from_user.id
    answer_message = appeal.get_appeals(user_id=user_id)
    await message.answer(answer_message)
