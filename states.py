from aiogram.fsm.state import StatesGroup, State

class CaseState(StatesGroup):
    question = State()
