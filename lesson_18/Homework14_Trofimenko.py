
class Train:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
        self.__add_traincar = dict()

    def __len__(self):
        return len(self.__add_traincar)

    def __setitem__(self, key, value):
        self.__add_traincar[key] = value

    def __getitem__(self, item):
        return self.__add_traincar[item]


class TrainCar:
    def __init__(self, traincar_number, passenger_name, passenger_place, destination):
        self.__traincar_number = traincar_number
        self.__passenger_name = passenger_name
        self.__passenger_place = passenger_place
        self.__destination = destination
        self.__add_passenger = dict()

    @property
    def get_passenger_data(self):
        return self.__traincar_number, self.__passenger_name, self.__passenger_place, self.__destination

    def __len__(self):
        return len(self.__add_passenger)

    def __setitem__(self, key, value):
        self.__add_passenger[key] = value

    def __getitem__(self, item):
        return self.__add_passenger[item]


traincar = TrainCar(0, 'Lokomotiv', 200, 'Depo')

traincar[1] = TrainCar(2, 'Tobby', 7, 'Kharkiv')
traincar[2] = TrainCar(3, 'Harry', 4, 'Kyiv')
traincar[3] = TrainCar(3, 'Harry', 4, 'London')
traincar[4] = TrainCar(4, 'Mathew', 8, 'Vena')

print(traincar[2])
print(len(traincar))

train = Train('Intercity', 200)
train[1] = traincar[1]
train[2] = traincar[2]
train[3] = traincar[3]
print(len(train))
print(train[1].get_passenger_data)
print(train[3].get_passenger_data)
