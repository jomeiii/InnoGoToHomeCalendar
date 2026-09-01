import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN
from handlers.start import router as start_router
from handlers.countdown import router as countdown_router
from handlers.settings import router as settings_router
from services.users import init_db
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from services.notifications import send_countdown

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)


async def main():
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(countdown_router)
    dp.include_router(settings_router)

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    scheduler.add_job(
        send_countdown,
        "cron",
        hour=9,
        minute=0,
        args=[bot]
    )

    init_db()

    scheduler.start()

    try:
        await dp.start_polling(bot)
    finally:
        scheduler.shutdown()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
