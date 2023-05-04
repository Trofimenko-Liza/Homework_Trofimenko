# task 1
class Chinachild:
    def __init__(self, name:str, gender:str):
        def inner(*args):
            print()
        return inner

def singleton(_class):
    def inner(*args):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args))
        return getattr(_class, 'instance')
    return inner

@singleton
class Chinachild:
        def __init__(self, name: str, gender: str):
            self.__name = name
            self.__gender = gender

child1 = Chinachild('Lian', 'girl')
child2 = Chinachild('Nguan', 'boy')
print()
del child2

# task 2

from abc import ABC, abstractmethod

class Dish(ABC):
    name: str = ''

    @abstractmethod
    def get_order(self, order:str):
        pass


class Rissoto(Dish):
    order: str = 'rissoto'
    def __init__(self):
        self.name = 'Rissoto'
        self.__possition = ['Seafood', 'Beef']

    def get_order(self, order):
        if order == 'Seafood':
            print('Rissoto with seafood')



class Pasta(Dish):
    order: str = 'pasta'

    def __init__(self):
        self.name = 'Pasta'
        self.__possition = ['Carbonara', 'Bolonies']

    @property
    def possition(self):
        return self.__possition

    def get_order(self, order):
        if order == 'Carbonara':
            print('Pasta Carbonara')


class Pizza(Dish):
    order: str = 'pizza'

    def __init__(self):
        self.name = 'Pizza'
        self.__possition = ['Margarita', 'Peperoni']

    @property
    def possition(self):
        return self.__possition

    def get_order(self, order):
        if order == 'Peperoni':
            print('Pizza Peperoni')

class AbstractDishFactory:

    @staticmethod
    def get_factory(order:str):
        if order == 'rissoto':
            return Rissoto()

        if order == 'pasta':
            return Pasta()

        if order == 'pizza':
            return Pizza()
        else:
            raise Exception('this dish is not on the menu')


order_rissoto = AbstractDishFactory.get_factory('rissoto')
order_pasta = AbstractDishFactory.get_factory('pasta')
order_pizza = AbstractDishFactory.get_factory('pizza')
order_rissoto.get_order('Seafood')
order_pizza.get_order('Peperoni')
order_pasta.get_order('Carbonara')






