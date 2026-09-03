from typing import Optional

from aiogram import F, Router, Bot
from aiogram.types import Message

from services.countdown import get_days_left
from services.photos import get_city_photo, get_city

router = Router()


async def send_countdown_message(
    bot: Bot,
    user_id: int,
    message: Optional[Message] = None
):
    days_left = get_days_left(user_id)
    city = get_city(user_id)
    photo = get_city_photo(city)

    text = f"🏠 До дома осталось <b>{days_left}</b> дней."

    if photo is None:
        if message:
            await message.answer(text)
        else:
            await bot.send_message(user_id, text)
        return

    if message:
        await message.answer_photo(
            photo=photo,
            caption=text
        )
    else:
        await bot.send_photo(
            chat_id=user_id,
            photo=photo,
            caption=text
        )


@router.message(F.text == "🏠 Сколько осталось?")
async def days_handler(message: Message):
    await send_countdown_message(
        bot=message.bot,
        user_id=message.from_user.id,
        message=message
    )

