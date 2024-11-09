import inspect
from pprint import pprint


def introspection_info(obj):
    result = {}
    result['type'] = type(obj).__name__
    result['module'] = getattr(obj, 'module', '__main__')
    result['attributes'] = []
    result['methods'] = []
    for arg in dir(obj):
        attr = getattr(obj, arg)
        if callable(attr):
            try:
                sig = inspect.signature(attr)
            except:
                sig = ''
            result['methods'].append(f'{arg}{sig}')
        else:
            result['attributes'].append(arg)
    return result


class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> str:
        return f"{self.year} {self.make} {self.model}"


number_info = introspection_info(42)
print(' Число:')
pprint(number_info)

list_info = introspection_info([1, 2, 3])
print('\n Список:')
pprint(list_info)

car = Car("Toyota", "Corolla", 2020)
objclass_info = introspection_info(car)
print('\n Экземпляр класса:')
pprint(objclass_info)
