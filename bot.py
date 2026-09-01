import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN
from handlers.start import router as start_router
from handlers.countdown import router as countdown_router
from handlers.subscribe import router as subscribe_router
from handlers.settings import router as settings_router
from services.users import init_db


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(countdown_router)
dp.include_router(subscribe_router)
dp.include_router(settings_router)

async def main():
    logger.info("Starting bot...")

    init_db()
    logger.info("Database initialized")

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    logger.info("Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())