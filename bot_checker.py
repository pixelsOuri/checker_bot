from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F
import logging
import contextlib , asyncio

# Токен бота и ID канала
BOT_TOKEN = '7729445470:AAHBQKAYsuzZNB2K5PnHwbE8F9nIIu-1-4M'
CHANNEL_ID = -1002374583339  # ID вашего канала

async def approve_request(chat_join: ChatJoinRequest,bot: Bot):
    await chat_join.approve()
async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot: Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id ==CHANNEL_ID)

    try:
        await dp.start_polling (bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f' [Exception] {ex}', exc_info=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())

