from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
	name = State()
	photo = State()
	phone_number = State()
	town = State()
	status_in_israel = State()
	sphere = State()
	site = State()
	instagram = State()
	facebook = State()
	linkedin = State()
	member = State()
	hobby = State()
	query = State()
	question = State()
