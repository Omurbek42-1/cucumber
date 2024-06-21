from aiogram import  Router, F, types 
from aiogram.filters.command import Command 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router() 


# FSM - Finite State Mashine  - Конечный автомат 
class BookSurvey(StatesGroup): 
    name = State() # имя пользователя 
    age = State() # возраст 
    gender = State() # пол 
    genre = State #  любимый жанр 


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message,state: FSMContext):  
    # устанавливаем состояние 
   await state.set_data(BookSurvey.name)
   await message.answer("Как вас зовут?")
   
   
@survey_router.message(Command("Stop")) 
@survey_router.message(F.text == "стоп") 
async def stop_survey(message: types.Message, State: FSMContext):  
    await state.clear()
    await message.answer("Опрос остановлен")
   
   
@survey_router.message(BookSurvey.name) 
async def process_name(message: types.Message, state: FSMContext):
    print("Message:", message.text)
    # сохраняем данные пользователя  
    await state.update_data(name=message.text)
    # устанавливаем состояние
    await state.set_state(BookSurvey.age)
    await message.answer("Сколько вам лет?") 
    
    
@survey_router.message(BookSurvey.age) 
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit(): 
        await message.answer("Пожалуйста введите цифры")
        return
    age = int(age)
    if age < 10 or > 90:   
        await message.answer("Введите возраст от 10 до 90")  
        return
    
        
    # сохраняем данные пользователя  
    await state.update_data(age=message.text) 
    # устанавливаем состояние
    await state.set_state(BookSurvey.gender) 
    await message.answer("Какого вы пола?")  
    
    
@survey_router.message(BookSurvey.gender) 
async def process_gender(message: types.Message, state: FSMContext):
    # сохраняем данные пользователя  
    await state.update_data(gender=message.text)
    # устанавливаем состояние
    await state.set_state(BookSurvey.genre)
    await message.answer("Ваш любимый жанр худ-литературы?")  
    
    
    
@survey_router.message(BookSurvey.genre) 
async def process_gender(message: types.Message, state: FSMContext):
     # сохраняем данные пользователя  
    await state.update_data(name=message.text)
    # сохраняем данные пользователя  
    await state.update_data(genre=message.text)
    
    data = await state.get_data() 
    print("Data", data)
    await state.clear() 
    await message.answer("Спасибо за прохождение опроса") 