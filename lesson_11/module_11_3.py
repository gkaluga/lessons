import inspect
from pprint import pprint

import requests


def introspection_info(obj):
    result = {}
    result['type'] = type(obj)
    result['module'] = inspect.getmodule(obj).__name__
    result['attributes'] = []
    result['methods'] = []
    for arg in dir(obj):
        if callable(getattr(obj, arg)):
            result['methods'].append(arg)
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

# car = Car("Toyota", "Corolla", 2020)
# print(introspection_info(car))
r = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre')
print(introspection_info(r))
