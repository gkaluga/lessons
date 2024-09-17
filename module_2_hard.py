def get_password(cipher):
    password = ''
    pairs_of_numbers = []
    for i in range(1, cipher-1):
        for j in range(i+1, cipher):
            sum = i + j
            if cipher % sum == 0:
                pairs_of_numbers.append([i, j])
                password += str(i) + str(j)
    return password, pairs_of_numbers

cipher = int(input('Введите шифр (3-20): '))
password, pairs_of_numbers = get_password(cipher)
print('Пары чисел:', pairs_of_numbers)
print('Пароль:', password)
