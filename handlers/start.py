from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.users import subscribe_user

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    if message.from_user is None:
        return

    subscribe_user(message.from_user.id)



    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        "🏠 Я помогу тебе узнать, сколько осталось до дома."
    )