

class Dog:
    def __init__(self, breed, name, age, colour, gender):
        self.breed = breed
        self.name = name
        self.age = age
        self.colour = colour
        self.gender = gender


    @staticmethod
    def say_woof():
        print('Woof-woof')

dog1 = Dog('Stafterier', 'Bars', 5, 'white', 'boy')
dog2 = Dog('Shpits', 'Aia', 3, 'beige', 'girl')
dog3 = Dog('Terier', 'Lucky', 11, 'brown', 'boy')

vote = Dog.say_woof()
print(dog2.breed, dog2.name, dog2.gender)
print(dog1.name, dog1.age, dog1.colour)
print(dog3.breed, dog3.name, dog3.age, dog3.colour, dog3.gender)

