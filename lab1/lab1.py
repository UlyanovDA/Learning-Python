# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Car:
    """Класс 'Авто', в котором атрибуты - его тех. харак-ки"""
    def __init__(self, hp: int, fuel: int, fuel_tank: int):
        """
        Создание и подготовка к работе объекта 'Car'
        :param hp: число лошадиных сил
        :param fuel: количество топлива в баке
        :param fuel_tank: объём бака

        Пример:
        >>> car = Car(150, 27, 50)
        """

        """Проверка на тип данных"""
        if not isinstance(hp, int):
            raise TypeError('Чило лошадиных сил д.б. типа int')
        """Проверка на тип данных"""
        if not isinstance(fuel, int):
            raise TypeError('Количество топлива д.б. типа int')
        """Проверка на тип данных"""
        if not isinstance(fuel_tank, int):
            raise TypeError('Объём бака д.б. типа int')
        '''Проверка на положительность харак. авто'''
        if hp < 0 or fuel < 0 or fuel_tank < 0:
            raise ValueError('Харак-ки авто д.б. положительными')

        self.hp = hp
        self.mpg = fuel
        self.tank = fuel_tank

    def refueling(self, add_fuel: int) -> None:
        """
        Метод для определения количества топлива в баке.

        :return: Количество топлива (fuel)

        Пример:
        >>> car = Car(150, 27, 50)
        >>> car.refueling(5)
        """
        if not isinstance(add_fuel, int):
            raise TypeError('Количество топлива д.б. типа int')
        ...


    def stage(self, new_hp: int) -> None:
        """
        Метод для определения мощности после тюнинга

        :return: новое число лошадиных сил new_hp (int)

        Пример:
        >>> car = Car(150, 27, 50)
        >>> car.stage(10)
        """
        if not isinstance(new_hp, int):
            raise TypeError('Чило лошадиных сил д.б. типа int')
        ...


class Rocket:
    """Класс "Ракета", в котором атрибуты - её харак-ки"""
    def __init__(self, payload: int, max_speed: int, crew: int):
        """
        Создание и подготовка к работе объекта 'Rocket'
        payload - грузоподъёмность
        max_speed - максимальная скорость
        crew - число членов экапижа

        Пример:
        >>> soyuz = Rocket(2000, 8000, 3)
        """

        """Проверка на тип данных"""
        if not isinstance(payload, int):
            raise TypeError('Грузоподъёмность д.б. типа int')
        """Проверка на тип данных"""
        if not isinstance(max_speed, int):
            raise TypeError('Max скорость д.б. типа int')
        """Проверка на тип данных"""
        if not isinstance(crew, int):
            raise TypeError('Число членов экипажа д.б. типа int')
        '''Проверка на положительность харак. ракеты'''
        if payload < 0 or max_speed < 0 or crew < 0:
            raise ValueError('Харак-ки ракеты д.б. положительными')

        self.payload = payload
        self.speed = max_speed
        self.crew = crew


    def weight_crew(self, weight: int) -> None:
        """
        Метод для опеределения массы экипижа.

        :return: значение грузоподъёмности с экипажом weight (int)

        Пример:
        >>> soyuz = Rocket(2000, 8000, 3)
        >>> soyuz.weight_crew(200)
        """
        if not isinstance(weight, int):
            raise TypeError('Масса д.б. типа int')
        if weight < 0:
            raise ValueError('Масса экипажа д.б. положительной')
        ...

    def space_velocity(self, velocity: float) -> None:
        """
        Скорость в ближнем космосе.

        :return: значение скорости velocity (float)

        Пример:
        >>> soyuz = Rocket(2000, 8000, 3)
        >>> soyuz.space_velocity(0.9)
        """
        if not isinstance(velocity, float):
            raise TypeError('Скорость д.б. типа float')
        ...


class Plane:
    """Класс "Самолёт", в котором его харак-ки"""
    def __init__(self, cost: int, seat_capacity:int):
        """
        Создание и подготовка к работе объекта 'Plane'
        cost - стоимость билета
        seat_capacity - кол-во посадочных мест

        Пример:
        >>> mc = Plane(10000, 200)
        """

        """Проверка на тип данных"""
        if not isinstance(cost, int):
            raise TypeError('Грузоподъёмность д.б. типа int')
        """Проверка на тип данных"""
        if not isinstance(seat_capacity, int):
            raise TypeError('Max скорость д.б. типа int')
        '''Проверка на положительность харак. самолёта'''
        if cost < 0 or seat_capacity < 0:
            raise ValueError('Харак-ки самолёта д.б. положительными')

        self.cost = cost
        self.seat = seat_capacity


    def cost_of_the_flight(self) -> None:
        """
        Метод для определения суммарной цены полёта всех пассажиров.

        :return: общую сумму sum_cost (int)

        Пример:
        >>> mc = Plane(10000, 200)
        >>> mc.cost_of_the_flight()
        """
        ...

    def occupied_place(self, oc_place: int) -> None:
        """
        Метод для определения числа занятых мест.

        :return: число занятых мест oc_place (int)

        Пример:
        >>> mc = Plane(10000, 200)
        >>> mc.occupied_place(100)
        """
        if not isinstance(oc_place, int):
            raise TypeError('Число мест д.б. типа int')
        if oc_place < 0:
            raise ValueError('Число мест д.б. положительным')


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
