import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatJoinRequest
from keep_alive import keep_alive

# Load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID", 0))  # Replace with your group/channel ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Start command
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("👋 Hello! I'm an auto-approve bot running on Render.")

# Handle join requests
@dp.chat_join_request_handler()
async def approve_join_request(join_request: ChatJoinRequest):
    user = join_request.from_user
    chat = join_request.chat

    # Approve the request
    await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)

    # Send a welcome message
    await bot.send_message(
        chat_id=chat.id,
        text=f"✅ Welcome {user.mention} to *{chat.title}*!",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    keep_alive()  # keep alive service
    executor.start_polling(dp, skip_updates=True)
