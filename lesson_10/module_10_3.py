from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            val = randint(50,500)
            self.balance += val
            # \n вставил в строку вывода, иначе другой поток периодически
            # выводил свой текст перед выводом перевода строки в текущем потоке
            print(f'Пополнение: {val}. Баланс: {self.balance}\n', end='')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.01)

    def take(self):
        for _ in range(100):
            val = randint(50,500)
            print(f'Запрос на {val}\n', end='')
            if self.balance >= val:
                self.balance -= val
                print(f'Снятие: {val}. Баланс: {self.balance}\n', end='')
            else:
                print('Запрос отклонён, недостаточно средств\n', end='')
                self.lock.acquire()
            sleep(0.01)



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
