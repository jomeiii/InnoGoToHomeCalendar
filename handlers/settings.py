from datetime import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.main import main_keyboard, settings_keyboard
from states.settings import SettingsState

from services.countdown import change_departure_time

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
        date = datetime.strptime(message.text, '%d-%m-%y').date()
    except ValueError:
        await message.answer(
            'Неверный формат даты.\n'
            'Введите дату в формате ДД-ММ-ГГ'
        )
        return

    await message.answer(
        f'Дата каникул установлена: {date.strftime("%d-%m-%Y")}',
        reply_markup=main_keyboard
    )

    await state.clear()
    change_departure_time(date)


@router.message(F.text == "◀️ Назад")
async def back(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        "Главное меню",
        reply_markup=main_keyboard
    )
