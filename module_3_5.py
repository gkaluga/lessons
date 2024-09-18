
def get_multiplied_digits(n):
    global stack
    if stack:
        print(*stack, sep=' * ', end=' * ')
    print(f'get_multiplied_digits({n}) -> ', end='')

    str_number = str(n)
    first = int(str_number[0])
    stack.append(first)
    if len(str_number) > 1:
        rest = int(str_number[1:])
        if rest > 1:
            return first * get_multiplied_digits(rest)

    print(*stack, sep=' * ')
    return first


stack = []
result = get_multiplied_digits(402050)
# Отражение на консоли рекурсивных вызовов функции:
# get_multiplied_digits(402050) -> 4 * get_multiplied_digits(2050) -> 4 * 2 * get_multiplied_digits(50) -> 4 * 2 * 5

print('Результат:',result)
# Результат: 40
