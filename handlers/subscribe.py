from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from services.users import subscribe_user, unsubscribe_user

router = Router()

@router.message(F.text == "🔔 Подписка")
async def subscribe(message: Message):
    await message.answer(f'Подписаться: /subscribe\n'
                         f'Отписаться: /unsubscribe')
@router.message(Command("subscribe"))
async def subscribe_handler(message: Message):
    if message.from_user is None:
        return

    subscribe_user(message.from_user.id)

    await message.answer("Вы подписались на рассылку.")

@router.message(Command("unsubscribe"))
async def unsubscribe_handler(message: Message):
    if message.from_user is None:
        return

    unsubscribe_user(message.from_user.id)

    await message.answer('Вы отписались от рассылки.')