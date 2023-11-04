from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
import time
import json

bot = Bot(token='6300660103:AAE58cLzoVYbrT7je8GC7bZF9P1Ma-5XF5o', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🔪Ножи', '🧤Перчатки', '︻デ═一 Снайпки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию "примечание: бот не выводит товары у которых нет ссылки"', reply_markup=keyboard)

@dp.message_handler(Text(equals='🔪Ножи'))
async def get_discount_knives(message: types.Message):
    await message.answer('Please wait a bit...')

    collect_data(cat_type=2)

    with open('result1.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: " )}{item.get("discount")}%\n' \
            f'{hbold("Цена до скидки: " )}${item.get("price_before_Discount")}\n' \
            f'{hbold("Цена со скидкой: " )}${item.get("computed_price")}\n' \
            f'{hbold("Флоат: " )}{item.get("float")}\n'
        
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals='🧤Перчатки'))
async def get_discount_gloves(message: types.Message):
    await message.answer('Please wait a bit...')

    collect_data(cat_type=13)

    with open('result1.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: " )}{item.get("discount")}%\n' \
            f'{hbold("Цена до скидки: " )}${item.get("price_before_Discount")}\n' \
            f'{hbold("Цена со скидкой: " )}${item.get("computed_price")}\n' \
            f'{hbold("Флоат: " )}{item.get("float")}\n'
        
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='︻デ═一 Снайпки'))
async def get_discount_guns(message: types.Message):
    await message.answer('Please wait a bit...')

    collect_data(cat_type=4)

    with open('result1.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: " )}{item.get("discount")}%\n' \
            f'{hbold("Цена до скидки: " )}${item.get("price_before_Discount")}\n' \
            f'{hbold("Цена со скидкой: " )}${item.get("computed_price")}\n' \
            f'{hbold("Флоат: " )}{item.get("float")}\n'
        
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()