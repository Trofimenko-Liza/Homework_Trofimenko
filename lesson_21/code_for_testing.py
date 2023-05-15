class Human:
    def __init__(self, name:str, age:int, hair_colour:str):
        self.__name = name
        self.__age = age
        self.__hair_colour = hair_colour

    def grow(self):
        self.__age +=1
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age


    def change_hair_colour(self, new_colour:str):
        if new_colour not in ["Red", "Green"]:
            raise Exception("You can not use this colour")
        self.__hair_colour = new_colour


    @property
    def colour(self):
        return self.__hair_colour
