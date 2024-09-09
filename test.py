# cars = ["Ford", "Volvo", "BMW"]
# print(cars.pop(1))
# print(cars)

# phone_book = {'denis': '00000000000', 'dasha': '1111111111'}
# print(phone_book.get('deni','3333333333'))
# itims = phone_book.items()
# print(type(itims)

# ml_libraries = set(("Pandas", "Pandas", "NumPy", "Keras", "TensorFlow"))
# print(ml_libraries)

# Все доступные книги (находящиеся в продаже)
# books_available = {"Fluent Python", "Python Cookbook", "Python crash course"}
# # Уже купленные книги
# books_purchased = {"Learning python", "Python in a nutshell", "Fluent Python"}
#
# print(books_available)
# print(books_available.pop())
# print(books_available.pop())
# print(books_available)
#
# books_total = books_available.union(books_purchased) # Все доступные и приобретенные книги
# print(books_total)
# books_popular = books_available.intersection(books_purchased) # Доступные книги, которые были куплены
# print(books_popular)
# books_sold_out = books_purchased.difference(books_available) # Раскупленные книги, которых уже нет в продаже
# print(books_sold_out)

# ip = "192.168.0.1"
# s = ip.split('.')
# print(s)
# print(*s)
# octets = [int(o) for o in s]
# r = "{:b}".format(3)
# print(r)

from time import sleep

a = 5
print(a)
print("я тут" )
sleep(4)
print("фух, 4 секунды прошло")
