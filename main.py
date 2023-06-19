from aiogram import Bot, Dispatcher, executor, types

from secret import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welkome(message: types.Message):
    await message.reply('Привет, я пока ничего не умею!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
