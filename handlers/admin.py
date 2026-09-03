from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from services.photos import get_pending_photo, approve_photo, reject_photo

router = Router()

ADMIN_ID = 860859651


@router.message(Command("admin"))
async def admin(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    photo = get_pending_photo()

    if photo is None:
        await message.answer("📭 Нет фотографий на модерации.")
        return

    photo_id, city, photo_file_id, uploaded_by = photo

    builder = InlineKeyboardBuilder()

    builder.button(
        text="✅ Одобрить",
        callback_data=f"approve:{photo_id}"
    )

    builder.button(
        text="❌ Отклонить",
        callback_data=f"reject:{photo_id}"
    )

    await message.answer_photo(
        photo=photo_file_id,
        caption=(
            f"🏙 Город: {city}\n"
            f"👤 Пользователь: {uploaded_by}\n"
            f"🆔 Фото: {photo_id}"
        ),
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data.startswith("approve:"))
async def approve(callback: CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        return

    photo_id = int(callback.data.split(":")[1])

    approve_photo(photo_id)

    await callback.answer("Фото одобрено ✅")
    await callback.message.edit_caption(
        caption="✅ Фото одобрено"
    )


@router.callback_query(F.data.startswith("reject:"))
async def reject(callback: CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        return

    photo_id = int(callback.data.split(":")[1])

    reject_photo(photo_id)

    await callback.answer("Фото отклонено ❌")
    await callback.message.edit_caption(
        caption="❌ Фото отклонено"
    )
