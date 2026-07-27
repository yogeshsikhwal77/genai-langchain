from typing import TypedDict

class Person(TypedDict):

    name : str
    age : int
    income: float

person : Person = {'name':'yogesh','age':19,'income':2.723}

print(person)