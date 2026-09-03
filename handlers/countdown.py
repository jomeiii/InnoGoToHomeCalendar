from aiogram import F, Router
from aiogram.types import Message

from services.countdown import get_days_left

from services.photos import get_city_photo, get_city


router = Router()


@router.message(F.text == '🏠 Сколько осталось?')
async def days_handler(message: Message):
    days_left = get_days_left(message.from_user.id)
    city = get_city(message.from_user.id)
    photo = get_city_photo(city)

    if photo is None:
        await message.answer(f"🏠 До дома осталось <b>{days_left}</b> дней.")
        return

    await message.answer_photo(
        photo=photo,
        caption=f"🏠 До дома осталось <b>{days_left}</b> дней."
    )