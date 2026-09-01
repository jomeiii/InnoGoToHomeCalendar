from aiogram import F, Router
from aiogram.types import Message

from services.countdown import get_days_left


router = Router()


@router.message(F.text == '🏠 Сколько осталось?')
async def days_handler(message: Message):
    days_left = get_days_left()

    await message.answer(
        f"🏠 До дома осталось <b>{days_left}</b> дней."
    )