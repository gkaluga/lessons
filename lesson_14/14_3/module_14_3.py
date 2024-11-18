from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from mypkg.changer import message

API = '6988926972:AAGrEvGc5JIgDW7KfJVcnwEqHvS7qmdd5dY'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# button1 = KeyboardButton('Расчитать')
# button2 = KeyboardButton('Информация')
markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Расчитать'),
            KeyboardButton('Информация')
        ],
        [KeyboardButton('Купить')]
    ],resize_keyboard=True, one_time_keyboard=True
)
# markup.add(button1, button2)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=markup)


inline_bt1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
inline_bt2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_menu = InlineKeyboardMarkup()
inline_menu.add(inline_bt1, inline_bt2)


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


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        with open(f'pills{i}r.png', 'rb') as img:
            await message.answer_photo(img, f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_buy_kb)


inline_buy_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('Product1', callback_data='product_buying1'),
        InlineKeyboardButton('Product2', callback_data='product_buying2'),
        InlineKeyboardButton('Product3', callback_data='product_buying3'),
        InlineKeyboardButton('Product4', callback_data='product_buying4')]
    ]
)


@dp.callback_query_handler(lambda c: c.data[0:14] == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer(f'Вы успешно приобрели "Product{call.data[14]}"!')


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
