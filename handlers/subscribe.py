from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("subscribe"))
async def subscribe(message: Message):
    await message.answer('Вы подписались на рассылку')

@router.message(Command("unsubscribe"))
async def unsubscribe(message: Message):
    await message.answer('Вы отписались от рассылки')