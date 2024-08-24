from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from filters.chat_filters import ChatTypeFilter
from common.functions import get_random_picture
import random

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

h = ['Hello', 'Hi', 'Good morning']
b = ['Bye', 'Take care', 'Goodbye']

@user_private_router.message(CommandStart())
async def cmd_star(message: Message):
    await message.answer(f"Hello {message.from_user.full_name}")

@user_private_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("You can print Hello or Bye to get answer or send photo")

@user_private_router.message(F.photo)
async def get_photo(message: Message):
    await message.reply('Photo')

@user_private_router.message(Command('random'))
async def cmd_random(message:Message):
    await message.reply("Catagory")
    a = message.text
    await message.answer_photo(get_random_picture(a))

#dz

@user_private_router.message(F.text == "Hello")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(h[i])

@user_private_router.message(F.text == "Good morning")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(h[i])

@user_private_router.message(F.text == "Hi")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(h[i])

@user_private_router.message(F.text == "Bye")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(b[i])

@user_private_router.message(F.text == "Take care")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(b[i])

@user_private_router.message(F.text == "Goodbye")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(b[i])