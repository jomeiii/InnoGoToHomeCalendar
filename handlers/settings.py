from datetime import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.main import main_keyboard, settings_keyboard
from states.settings import SettingsState

from services.users import set_departure_date

router = Router()


@router.message(F.text == '⚙️ Настройки')
async def settings(message: Message):
    await message.answer(
        'Настройки',
        reply_markup=settings_keyboard
    )


@router.message(F.text == '📅 Изменить дату каникул')
async def change_date(message: Message, state: FSMContext):
    await message.answer(
        'Введите дату в формате ДД-ММ-ГГ'
    )

    await state.set_state(SettingsState.waiting_for_date)


@router.message(SettingsState.waiting_for_date)
async def process_date(message: Message, state: FSMContext):
    try:
        departure_date = datetime.strptime(
            message.text,
            "%d-%m-%y"
        ).date()
    except ValueError:
        await message.answer(
            "❌ Неверный формат.\n"
            "Введите дату в формате ДД-ММ-ГГ"
        )
        return

    if message.from_user is None:
        return

    set_departure_date(
        message.from_user.id,
        departure_date.isoformat()
    )

    await state.clear()

    await message.answer(
        "✅ Дата успешно изменена!",
        reply_markup=main_keyboard
    )


@router.message(F.text == "◀️ Назад")
async def back(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        "Главное меню",
        reply_markup=main_keyboard
    )
