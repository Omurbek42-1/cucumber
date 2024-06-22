from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup

class ReviewStates(StatesGroup):
    start_review = State()
    get_name = State()
    get_contact = State()
    get_visit_date = State()
    get_food_quality = State()
    get_cleanliness = State()
    get_extra_comments = State()

# Обработчики для каждого состояния
@dp.message_handler(commands=['start'])
async def start_review(message: types.Message):
    await ReviewStates.start_review.set()
    await message.reply("Добро пожаловать! Давайте начнем процесс отзыва. Как вас зовут?")

@dp.message_handler(state=ReviewStates.get_name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await ReviewStates.next()
    await message.reply("Как можно связаться с вами? (Номер телефона или Instagram)")

# Реализуйте аналогичные обработчики для остальных состояний (контакт, дата посещения, оценки, комментарии)

# Запуск опроса обновлений
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
