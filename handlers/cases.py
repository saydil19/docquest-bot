import json
import random
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import CaseState
from keyboards import next_case_keyboard

router = Router()

with open("cases.json", encoding="utf-8") as f:
    CASES = json.load(f)

@router.message(lambda m: m.text == "🩺 Клинический кейс")
@router.message(lambda m: m.text == "➡️ Следующий кейс")
async def start_case(message: Message, state: FSMContext):
    case = random.choice(CASES)

    await state.update_data(
        case=case,
        step=0,
        answers=[]
    )

    await message.answer(
        f"📋 Клинический случай:\n\n{case['complaint']}"
    )

    await message.answer(
        f"🤖 ИИ спрашивает:\n{case['questions'][0]}"
    )

    await state.set_state(CaseState.question)

@router.message(CaseState.question)
async def process_question(message: Message, state: FSMContext):
    data = await state.get_data()
    step = data["step"]
    case = data["case"]
    answers = data["answers"]

    answers.append(message.text)
    step += 1

    if step < len(case["questions"]):
        await state.update_data(step=step, answers=answers)
        await message.answer(
            f"🤖:\n{case['questions'][step]}"
        )
    else:
        await message.answer(
            "🧠 Разбор клинического мышления:\n\n"
            f"{case['result']}",
            reply_markup=next_case_keyboard()
        )
        await state.clear()
