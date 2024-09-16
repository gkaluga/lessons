def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
# Вывод на консоль:1 строка True

print_params('1-st parameter')
# Вывод на консоль:1-st parameter строка True

print_params('1-st parameter', '2-nd parameter')
# Вывод на консоль:1-st parameter 2-nd parameter True

print_params('1-st parameter', '2-nd parameter', '3-rd parameter')
# Вывод на консоль:1-st parameter 2-nd parameter 3-rd parameter

print_params(b = 25)
# Вывод на консоль:1 25 True

print_params(c = [1,2,3])
# Вывод на консоль:1 строка [1, 2, 3]

values_list = [100, 'hundred', False]
print_params(*values_list)
# Вывод на консоль:100 hundred False

values_dict = {'a': 'example', 'b': 3.14, 'c': 999}
print_params(**values_dict)
# Вывод на консоль:example 3.14 999

values_list_2 = [0.05, 'Symbols']
print_params(*values_list_2, 42)
# Вывод на консоль:0.05 Symbols 42
