from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main import main_keyboard
from services.users import subscribe_user


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    subscribe_user(message.from_user.id)

    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}! 👋\n\n"
        "Я буду считать, сколько осталось до дома 🏠",
        reply_markup=main_keyboard
    )