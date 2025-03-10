from typing import Type
from .classes import Category


def get_objects(data: list, category_class: Type[Category]) -> Category:
    objects = []
    for element in data:
        obj = category_class(element)
        objects.append(obj)
    return objects
