from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *


initiate_db()
API = '6988926972:AAGrEvGc5JIgDW7KfJVcnwEqHvS7qmdd5dY'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Расчитать'),
            KeyboardButton('Информация')
        ],
        [KeyboardButton('Купить')]
    ],resize_keyboard=True, one_time_keyboard=True
)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=markup)


inline_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
        ]
    ]
)


@dp.message_handler(text='Расчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu)


@dp.callback_query_handler(lambda c: c.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = round(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма каллорий: {calories}')
    await state.finish()
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=markup)


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for p in products:
        i = p[1][-1]
        with open(f'pills{p[0]}r.png', 'rb') as img:
            await message.answer_photo(img, f'Название: {p[1]} | Описание: {p[2]} | Цена: {p[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_buy_menu)


inline_buy_menu = InlineKeyboardMarkup(row_width=4)
for p in get_all_products():
    inline_buy_menu.insert(InlineKeyboardButton(p[1], callback_data=f'product_buying{p[0]}'))


@dp.callback_query_handler(lambda c: c.data[0:14] == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer(f'Вы успешно приобрели "{get_product(int(call.data[14:]))[1]}"!')


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
