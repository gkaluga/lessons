first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and first == third:
    print('\nРезультат:', 3)
elif first == second or first == third or second == third:
    print('\nРезультат:', 2)
else:
    print('\nРезультат:', 0)