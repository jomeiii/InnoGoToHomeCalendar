import logging

from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from services.users import subscribe_user


router = Router()

logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def start_handler(message: Message):
    logger.info(
        "User started bot: id=%s, name=%s",
        message.from_user.id,
        message.from_user.full_name
    )

    subscribe_user(message.from_user.id)

    logger.info(
        "User subscribed: id=%s",
        message.from_user.id
    )

    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}! 👋\n\n"
        "Ты подписан на рассылку."
    )