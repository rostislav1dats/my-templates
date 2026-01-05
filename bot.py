import asyncio
import logging 
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import user_handlers
from middlewares.whitelist import WhitelistMiddleware

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.message.outer_middleware(WhitelistMiddleware())

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')