class Cars:
    def __init__(self, wheels: int, power: int, weight: float):
        """Класс автомобили, который имеет атрибуты - число колёс,
        мощность и вес

        :param wheels: число колёс, шт.
        :param power: мощность, л.с.
        :param weight: вес, т.
        """
        self.wheels = wheels
        self.power = power
        self.weight = weight

    def pow_on_wheels(self):
        """Метод, который вычисляет удельную мощность на каждом колесе

        :return: удельная мощность, л.с.
        """
        return self.power / self.wheels

    def category(self):
        """Метод, который определяет, к какой категории относится
        авто, исходя из его веса

        :return: категория авто - легковой или грузовой
        """
        if self.weight <= 3.5:
            return print('легковой')
        else:
            return print('грузовой')

    def __str__(self) -> str:
        return f"Авто имеет {self.wheels} колеса"

    def __repr__(self) -> str:
        return f"Cars(wheels={self.wheels})"


class Usual(Cars):
    def __init__(self, wheels: int, power: int, weight: float, seats: int):
        """Класс обычных авто, который имеет доп. атрибут - число
        посадочных мест внутри

        :param seats: число посадочных мест, шт.
        """
        self.seats = seats
        super().__init__(wheels, power, weight)

    def __str__(self) -> str:
        return f"Авто имеет {self.seats} места"

    def __repr__(self) -> str:
        return f"Cars(seats={self.seats})"

    def pow_on_wheels(self):
        """Метод, который вычисляет удельную мощность на задней паре колёс

        :return: удельная мощность заднего привода, л.с.
        """
        return self.power / (self.wheels / 2)


class Race(Cars):
    def __init__(self, wheels: int, power: int, weight: float, speed: int):
        """Класс гоночных авто, который имеет доп. атрибут - макс.
        скорость. Этот атрибут для болидов более важен, чем для обычных авто

        :param speed: макс. скорость, км/ч
        """
        self.speed = speed
        super().__init__(wheels, power, weight)

    def __str__(self) -> str:
        return f"Макс. скорость авто {self.speed} км/ч"

    def __repr__(self) -> str:
        return f"Cars(speed={self.speed})"

    def pow_on_wheels(self):
        """При выводе результата показывается пояснение"""
        return print(f"Болид имеет {self.power / self.wheels} л.с. "
                     f"на каждом колесе")


if __name__ == "__main__":
    # Write your solution here
    vesta = Usual(4, 106, 1.3, 5)
    print(repr(vesta))
    vesta.category()

    print()

    vesta_rosneft = Race(4, 400, 1.25, 275)
    print(f"{vesta_rosneft}")
    vesta_rosneft.pow_on_wheels()

    pass
