class Product:
    """   Класс продукты   """

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    """   Класс магазин   """

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        product_text = file.read()
        file.close()
        return product_text

    def add(self, *products):
        product_text = self.get_products()
        add_text = ''
        for product in products:
            if '\n' + product.name + ', ' in '\n' + product_text:
                print(f'Продукт {product} уже есть в магазине')
            else:
                add_text += '\n' + str(product)

        if add_text:
            if not product_text:
                add_text = add_text[1:]
            file = open(self.__file_name, 'w')
            file.write(product_text + add_text)
            file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
