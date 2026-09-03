from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.main import main_keyboard
from services.users import subscribe_user, set_city

from states.settings import SettingsState

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    if message.from_user is None:
        return

    subscribe_user(message.from_user.id)

    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        "🏠 Я помогу тебе узнать, сколько осталось до дома.\n"
        "Напиши город, в который ты поедешь."
    )

    await state.set_state(SettingsState.waiting_for_city)


@router.message(SettingsState.waiting_for_city)
async def process_city(message: Message, state: FSMContext):
    if message.from_user is None:
        return
    if message.text is not None:
        city = message.text.strip()
    set_city(message.from_user.id, city.lower())
    await state.clear()
    await message.answer(f"✅ Город сохранён: {city}",
                         reply_markup=main_keyboard)
