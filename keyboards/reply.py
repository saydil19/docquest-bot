from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🩺 Клинический кейс")]
        ],
        resize_keyboard=True
    )

def next_case_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➡️ Следующий кейс")]
        ],
        resize_keyboard=True
    )
