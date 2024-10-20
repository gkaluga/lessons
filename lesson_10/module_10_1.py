from datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


if __name__ == '__main__':
    word_counts = [10, 30, 200, 100]
    start_time = datetime.now()
    for i in range(4):
        write_words(word_counts[i], f'example{i + 1}.txt')
    print(f'Работа функций {datetime.now() - start_time}')

    start_time = datetime.now()
    threads = [Thread(target=write_words, args=(word_counts[i], f'example{i + 5}.txt')) for i in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Работа потоков {datetime.now() - start_time}')
