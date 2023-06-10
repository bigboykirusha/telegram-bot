from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6290302605:AAGyto2kLbzqA4L2yX3Bqg-rmIOSccir2OA"
MSG = "TATAKA! TATAKAE!, {}!"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
photo = open('./assets/tatakae.jpg', 'rb')


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await bot.send_photo(user_id, photo, caption=MSG.format(user_name))

if __name__ == '__main__':
    executor.start_polling(dp)
