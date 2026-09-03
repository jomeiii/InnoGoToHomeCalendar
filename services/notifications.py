from aiogram import Bot

from services.countdown import get_days_left
from services.users import get_subscribed_users

from handlers.countdown import send_countdown_message

async def send_countdown(bot: Bot):
    users = get_subscribed_users()

    for user_id in users:
        try:
            await send_countdown_message(bot, user_id)
        except Exception as e:
            print(f"Не удалось отправить сообщение {user_id}: {e}")
