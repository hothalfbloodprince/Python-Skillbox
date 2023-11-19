class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if isinstance(coordinates, tuple) and len(coordinates) == 2:
            self.__coordinates = coordinates
        else:
            raise ValueError("Некорректные координаты")

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if isinstance(speed, int) and speed >= 0:
            self.__speed = speed
        else:
            raise ValueError("Некорректная скорость")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand
        else:
            raise ValueError("Некорректное название бренда")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            raise ValueError("Некорректный год")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if isinstance(number, str):
            self.__number = number
        else:
            raise ValueError("Некорректный номер")

    def __str__(self):
        return f"Трнаспорт: координаты: {self.coordinates}, скорость: {self.speed}, бренд: {self.brand}, год: {self.year}, номер: {self.number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self.coordinates[0] <= pos_x + length and pos_y <= self.coordinates[1] <= pos_y + width


class Passenger():
    def __init__(self):
        self.__passengers_capacity = 0
        self.__number_of_passengers = 0

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int) and passengers_capacity >= 0:
            self.__passengers_capacity = passengers_capacity
        else:
            raise ValueError("Некорректная вместимость пассажиров")

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and number_of_passengers >= 0:
            self.__number_of_passengers = number_of_passengers
        else:
            raise ValueError("Некорректное количество пассажиров")


class Cargo():
    def __init__(self):
        self.__carrying = 0

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int) and carrying >= 0:
            self.__carrying = carrying
        else:
            raise ValueError("Некорректная грузоподъемность")


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height >= 0:
            self.__height = height
        else:
            raise ValueError("Некорректная высота")


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.__port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            self.__port = port
        else:
            raise ValueError("Некорректное название порта")


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
