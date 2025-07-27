import asyncio
from aiogram import Bot, Dispatcher

from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN
from weather import get_weather

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('weather'))
async def weather(message: Message):
    city = 'Москва'
    data = get_weather('city')
    temp = round(data['main']['temp'])
    descr = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = round(data['wind']['speed'])
    msg = (f"Погода в городе {city}:\n"
           f"{descr.capitalize()}\n"
           f"Температура: {temp}°C\n"
           f"Влажность: {humidity}%\n"
           f"Ветер: {wind} м/с")
    await message.answer(msg)

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Бот умеет выполнять команды:\n/start\n/help\n/weather")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я учебный бот, я могу отправлять прогноз погоды!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен!")
    asyncio.run(main())