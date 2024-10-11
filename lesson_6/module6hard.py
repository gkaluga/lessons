from math import pi


class Figure:
    """   Класс фигуры (родительский)   """

    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return  r in range(0, 256) and g in range(0, 256) and b in range(0, 256)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and not [s for s in sides if not isinstance(s, int) or s <= 0]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    """   Класс круга   """

    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = (1)
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    """   Класс треугольника   """

    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = (1, 1, 1)
        super().__init__(color, *sides)

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return pow(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]), 0.5)

class Cube(Figure):
    """   Класс куба   """
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            side = sides[0]
        else:
            side = 1
        sides = (side for i in range(12))
        super().__init__(color, *sides)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle1 = Triangle((50, 60, 70), 3, 4, 5)
    triangle2 = Triangle((10, 20, 30), 20, 30)  # должен быть со сторонами [1, 1, 1]

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    triangle2.set_sides(5.5, 2, 4)  # Не изменится
    print(triangle2.get_sides())

    # Проверка периметра (круга, треугольника), это и есть длина:
    print(len(circle1))
    print(len(triangle2))

    # Проверка площади (круга, треугольника):
    print(circle1.get_square())
    print(triangle1.get_square())

    # Проверка объёма (куба):
    print(cube1.get_volume())

