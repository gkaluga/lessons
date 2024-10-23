from datetime import datetime
from multiprocessing import Process


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__' :
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_dt = datetime.now()
    for fname in filenames:
        read_info(fname)
    print(f'{datetime.now() - start_dt} (линейный)')
    # Вывод на консоль: 0:00:07.095783 (линейный)

    # Многопроцессный
    start_dt = datetime.now()
    processes = [Process(target=read_info, args=(fname,)) for fname in filenames]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print(f'{datetime.now() - start_dt} (многопроцессный)')
    # Вывод на консоль: 0:00:02.847357 (многопроцессный)