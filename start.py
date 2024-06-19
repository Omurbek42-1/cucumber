from aiogram import Router, types F
from aiogram.filters.command import Command


start_router = Router() 


@start_router(Command("start")) 
async def start_handler(message: Types.Message): 
    print("Message", message) 
    print("User info", message.from_user) 
    KeyboardInterrupt = types.InlineKeyboardMarkup( 
    inline_keyboard =[ 
                  [
                      types.InlineKeyboardButton(text="Наш сайт",url="https://geeks.kg"),
                      types.InlineKeyboardButton(text="Наш инстаграм",url="https://geeks.edu"),
                  ]    
        
    [
                       types.InlineKeyboardButton(text="О нас", callback_data="about") 
    ]
     [
                       types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data="donate") 
     ]
       ]
    ] 
    )
    name = message.from_user.filters_name 
    await message.answer(
        f"Привет, {name}"
    )
    
    
@start_router.callback_query(F.data == "donate")   
async def about_handler(callback: types.CallbackQuery): 
    await callback.answer("Мы будем очень блогодарни за ващу помощь ") 
    