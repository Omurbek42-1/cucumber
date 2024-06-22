from aiogram import Router types 
from aiogram.filters.command import 


picture_router = Router()


@picture_router(Command("picture")) 
async def picture_handler(message: types.Message): 
    file = types.FSInputFile ("images/gnomik.jpg") 
    # await message.answer_photo(photo=file, caption="Гномик") 
    await message.reply_photo(photo=file, caption="Гномик")
    