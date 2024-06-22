import asyncio 
from aiogram import Bot, Dispatcher, types 
from aiogram.filters.command import Command 
from dotenv import load_dotenv  
from os import getenv 
import logging


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN")) 
dp = Dispatcher() 


@dp.massage() 
async def echo_handler (message: types.Message):
    #print("Message",message) 
    print("User info", message,from_user) 
    
    
    name =  message.from_user.first_name
    await message.answer( 
        f"Привет, {name}"
        ) 
    
    
@dp.message(Command("picture"))
async def picture_handler(message: types.Message):
    file = types.FSInputFile("images/dog.jpg") 
    await message.answer_photo(photo=file, caption="Dog")
    
@dp.message(Command("start")) 
async def start_handler(message: types.Message):   
    await message.answer ("Привет!") 


async def main(): 
  # запускаем бот