
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        self.engine = None
        self.colour = None
        self.year = None

    def moving(self):
        print('moving')

    def stop(self):
        print('stop')

    @abstractmethod
    def overtake(self):
        print('to overtake')


class Skoda(Car):
    def __init__(self):
        super().__init__()


class Rapid(Skoda):
    def __init__(self):
        self.engine = 'Turbo-petrol'
        self.colour = 'White'
        self.year = 2019

    def overtake(self):
        print('Rapid: go to overtake')

class Octavia(Skoda):
    def __init__(self):
        self.engine = 'Diesel'
        self.colour = 'Silver'
        self.year = 2008

    def overtake(self):
        print("Octavia: i'm so old, i can't overtake")

class Fabia(Skoda):
    def __init__(self):
        self.engine = 'Gas'
        self.colour = 'Green'
        self.year = 2013

    def overtake(self):
        print('Fabia: it is very difficult for me to overtake')

rapid = Rapid()
octavia = Octavia()
fabia = Fabia()
print(rapid.year)
fabia.overtake()
octavia.overtake()
rapid.overtake()

