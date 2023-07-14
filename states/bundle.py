from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
	name = State()
	username = State()
	phone_number = State()
	photo = State()
	about = State()
	family = State()
	hobby = State()
	additional = State()
