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
        self.__new_exhibit = 'Kobzar'

    def add_new_exhibit(self):
        return self.__new_exhibit


class Italian_section(Museum):
    def __init__(self):
        super().__init__()
        self.exhibit = 'David Michelangelo'
        self.picture = 'The Last Supper by Leonardo da Vinci'
        self.household_item = 'Ancient Rome clothing'
        self.__new_exhibit = 'Sistine Madonna'

    def add_new_exhibit(self):
        return self.__new_exhibit


class France_section(Museum):
    def __init__(self):
        super().__init__()
        self.exhibit = 'Venus Milos'
        self.picture = 'Mona Lisa'
        self.household_item = 'Clothes of ancient Galia'
        self.__new_exhibit = 'Victoire de Samothrace'

    def add_new_exhibit(self):
        self.__prepare_place()
        self.__get_permissions_to_delivery()
        self.__get_logistic()
        return self.__new_exhibit

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
    def exhibit(self, value):
        self._exhibit = value


'''
    @exhibit.setter
    def exhibit(self, new_exponat):
        self.exhibit = new_exponat


    def change_picture(self, new_picture):
        self._picture = new_picture

    @property
    def picture(self):
        return self._picture
'''
