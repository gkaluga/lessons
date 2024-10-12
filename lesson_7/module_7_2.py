def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    number_of_line = 0
    result = {}
    for s_ in strings:
        number_of_line += 1
        key = (number_of_line, file.tell())
        result[key] = s_
        file.write(s_ + '\n')
    file.close()
    return result


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
