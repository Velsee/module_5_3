class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if 0 < new_floor <= self.number_of_floors:
            # Вывод последовательности чисел от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Сообщение об ошибке
            print("Такого этажа не существует")

    # __len__(self) - должен возвращать кол - во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __add__(self, value): # увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
        if isinstance(value, House):
            self.number_of_floors += value
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self

    # __radd__(self, value), __iadd__(self, value) - работают так же
    # как и __add__ (возвращают результат его вызова).
    def __radd__(self, value):
        self.__add__(value)
        return self

    def __iadd__(self, value):
        self.__add__(value)
        return self



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

