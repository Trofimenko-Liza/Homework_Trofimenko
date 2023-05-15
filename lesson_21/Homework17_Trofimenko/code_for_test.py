from abc import ABC, abstractmethod

class Museum(ABC):
    def __init__(self):
        self.exhibit = None
        self.picture = None
        self.household_item = None

    @abstractmethod
    def add_new_exhibit(self):
        pass

    class Ukranian_section(Museum):
        def __init__(self):
            super().__init__()
            self.exhibit = 'Scythian gold'
            self.picture = 'Black Square Malevich'
            self.household_item = 'Clothes of Kievska Rus'
            self.__new_exhibit = 0

        def add_new_exhibit(self):
            print('Kobzar Shevchenko')

    class Italian_section(Museum):
        def __init__(self):
            super().__init__()
            self.exhibit = 'David Michelangelo'
            self.picture = 'The Last Supper by Leonardo da Vinci'
            self.household_item = 'Ancient Rome clothing'
            self.__new_exhibit = 0

        def add_new_exhibit(self):
            print('Sistine Madonna')

    class France_section(Museum):
        def __init__(self):
            super().__init__()
            self.exhibit = 'Venus Milos'
            self.picture = 'Mona Lisa'
            self.household_item = 'Clothes of ancient Galia'
            self.__new_exhibit = 0

    def add_new_exhibit(self):
        self.__prepare_place()
        self.__get_permissions_to_delivery()
        self.__get_logistic()
        print('Victoire de Samothrace')
        self.__new_exhibit = 0

    def __prepare_place(self):
        print('Prepare a place for a new exhibit')

    def __get_permissions_to_delivery(self):
        print('Obtaining permits for moving the exhibit')

    def __get_logistic(self):
        print('Prepare transport for moving the exhibit')


    @property
    def exhibit(self):
        return self.exhibit

    @exhibit.setter
    def exhibit(self, new_exponat):
        self.exhibit = new_exponat


    def change_picture(self, new_picture):
        self._picture = new_picture




#    def change_household_item(self, new_household:str):
 #       self.household_item = new_household


new_exponat = Italian_section()
new_exponat.exhibit = 'New exhibit'
print(new_exponat.exhibit)


ukrainian_museum = Ukranian_section()

print(ukrainian_museum.household_item)
print(ukrainian_museum.picture)
ukrainian_museum.exhibit

italian_museum = Italian_section()

italian_museum.picture
print(italian_museum.picture)

france_museum = France_section()

print(france_museum.picture)
france_museum.add_new_exhibit()

ukrainian_museum.add_new_exhibit()

italian_museum.add_new_exhibit()
