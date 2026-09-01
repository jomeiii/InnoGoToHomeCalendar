from aiogram import Bot

from services.countdown import get_days_left
from services.users import get_subscribed_users


async def send_countdown(bot: Bot):
    users = get_subscribed_users()
    days_left = get_days_left()

    for user_id in users:
        try:
            await bot.send_message(
                user_id,
                f"🏠 До дома осталось <b>{days_left}</b> дней!"
            )
        except Exception as e:
            print(f"Не удалось отправить сообщение {user_id}: {e}")