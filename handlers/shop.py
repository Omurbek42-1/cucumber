from email import message
from aiogram import Router, F, types
from aiogram.filters.command import Command 


shop_router = Router() m


@shop_router.message(Command("magazin")) 
async def show_shop(message: types.Message): 
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Фантастика")
            ],
            [
                types.KeyboardButton(text="Драма"),
                types.KeyboardButton(text="Комедия")
            ]
        ]   
            resize_keyboard=True
    )
    await message.answer("Выберите жанр ниже", reply_markup=kb) 
    
    
@shop_router.message(F.text == "Фантастика") 
async def show_fantastic(message: types.Message): 
    print(message.text) 
    kb = types.ReplyKeyboardRemove() 
    await message.answer("Наши книги из жанра фантастика")
    
    
@shop_router.message(F.text == "Драма") 
async def show_fantastic(message: types.Message): 
    kb = types.ReplyKeyboardRemove() 
    await message.answer("Наши книги из жанра драма", reply_markup = kb)    