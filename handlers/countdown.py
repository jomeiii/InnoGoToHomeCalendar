from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.countdown import get_days_left


router = Router()


@router.message(Command("days"))
async def days_handler(message: Message):
    days_left = get_days_left()

    await message.answer(
        f"🏠 До дома осталось {days_left} дней."
    )