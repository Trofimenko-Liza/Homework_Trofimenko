# task 1
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



# task 2

class Scrumcompany:
    def __init__(self,
                 first_name:str=None,
                 last_name:str=None,
                 city:str=None,
                 title:str=None,
                 work_experience:int=None
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.title = title
        self.work_experience = work_experience

    @classmethod
    def new_employee(cls, first_name, last_name, title):
        return(first_name, last_name, title)

employee1 = Scrumcompany('Eva', 'Martynenko', 'Kharkiv', 'Account_Manager', 1)
employee2 = Scrumcompany('Alex', 'Stepanuk', 'Poltava', 'Java_developer', 4)
employee3 = Scrumcompany('Bogdana', 'Urchenko', 'Kyiv', 'HR', 3)

new_employee = Scrumcompany('Natalia', 'Butsko', 'Designer')

print(employee1.first_name, employee1.last_name, employee1.title)
print(employee2.first_name, employee2.last_name)
print(employee3.title, employee3.city)
print(new_employee.last_name)



