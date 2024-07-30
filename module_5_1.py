class House:                                       # Создайте класс House
    def __init__(self, name, number_of_floors):     # Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения
        self.name = name                            # Создайте атрибуты объекта self.name и
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):                      # Создайте метод go_to с параметром new_floor
        for i in range(1, new_floor + 1):            # Выведите на экран сообщение о том, что вы переходите на этаж
            if 1 <= i <= self.number_of_floors:
                print(f"{i} этаж дома")
            else:
                print(f'"Такого этажа не существует"')
                break


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
