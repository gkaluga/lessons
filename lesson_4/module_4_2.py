def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()
# Запуск функции inner_function внутри функции test_function отрабатывает нормально.
# Вывод на консоль: Я в области видимости функции test_function

inner_function()
# Запуск функции inner_function вне функции test_function вызывает ошибку:
# NameError: name 'inner_function' is not defined.