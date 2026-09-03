from aiogram.fsm.state import State, StatesGroup


class SettingsState(StatesGroup):
    waiting_for_date = State()
    waiting_for_city = State()