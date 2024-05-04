import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import r

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(r)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())