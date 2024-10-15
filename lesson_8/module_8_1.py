def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as exc:
        if exc.args[0][0:24] == 'can only concatenate str':
            return a + str(b)
        elif exc.args[0][0:34] == 'unsupported operand type(s) for +:':
            return str(a) + b
        else:
            print(exc)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.457, 7))
