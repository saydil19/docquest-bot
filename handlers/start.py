from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.reply import main_menu

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "👋 Добро пожаловать в DocQuest!\n\n"
        "Это тренажёр клинического мышления.\n"
        "Ты будешь анализировать пациентов как настоящий врач.",
        reply_markup=main_menu()
    )
