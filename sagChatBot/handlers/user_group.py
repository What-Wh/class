from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from filters.chat_filters import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

bad_words = {'fuck', 'bitch', 'idiot'}

@user_group_router.message()
@user_group_router.edited_message()
async def check_words(message:Message):
    if bad_words.intersection(set(message.text.lower().split())):
        # await message.delete()
        # await  message.text.replace(message.text, "***")
        await message.answer("Bad words")
    else:
        await message.answer("Everything is okey")