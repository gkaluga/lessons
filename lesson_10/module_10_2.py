from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies:
            enemies -= self.power
            days += 1
            if days == 1:
                wdays = 'день'
            elif days < 5:
                wdays = 'дня'
            else:
                wdays = 'дней'
            print(f'{self.name} сражается {days} {wdays}..., осталось {enemies} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} {wdays}!')


if __name__ == '__main__':
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    # Вывод строки об окончании сражения
    print('Все битвы закончились!')
