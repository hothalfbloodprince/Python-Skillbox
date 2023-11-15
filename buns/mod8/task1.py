class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        return f"coordinates: {self.coordinates}, speed: {self.speed}, brand: {self.brand}, year: {self.year}, number: {self.number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self.coordinates[0] <= pos_x + length and pos_y <= self.coordinates[1] <= pos_y + width


class Passenger:
    def __init__(self):
        self.__passengers_capacity = 0
        self.__number_of_passengers = 0

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self):
        self.__carrying = 0

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass


class Seaplane(Plane, Ship):
    pass
