import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import start, cases

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(cases.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
