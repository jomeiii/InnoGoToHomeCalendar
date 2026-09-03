from aiogram import F, Router
from aiogram.types import Message

from services.photos import add_photo
from services.users import get_city

router = Router()


@router.message(F.text == "📷 Предложить фото")
async def suggest_photo(message: Message):
    if message.from_user is None:
        return

    city = get_city(message.from_user.id)

    if city is None:
        await message.answer(
            "Сначала укажи свой город в настройках."
        )
        return

    await message.answer(
        f"📷 Отправь фотографию города {city}."
    )


@router.message(F.photo)
async def receive_photo(message: Message):
    if message.from_user is None:
        return

    city = get_city(message.from_user.id)

    if city is None:
        await message.answer(
            "Сначала укажи свой город в настройках."
        )
        return

    photo_file_id = message.photo[-1].file_id

    add_photo(
        city=city,
        photo_file_id=photo_file_id,
        uploaded_by=message.from_user.id
    )

    await message.answer(
        "✅ Фотография отправлена на модерацию!"
    )