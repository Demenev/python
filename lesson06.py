# Задание 1.
import time
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        while True:
            for i in TrafficLight.__color:
                if i == 'Красный':
                    print(i)
                    time.sleep(7)
                elif i == 'Желтый':
                    print(i)
                    time.sleep(2)
                else:
                    print(i)
                    time.sleep(20)
                    print(TrafficLight.__color[-2])
                    time.sleep(2)

t = TrafficLight()
t.running()

# Задание 2.
class Road:
    def determination_mass(self, length, width):
        self._length = length
        self._width = width
        print(f'Масса асфальта на дорогу длиной {self._width} м и длиной {self._length} м равна {(self._width * self._length * 25 * 5)/1000} тн')

m = Road()
m.determination_mass(5000, 20)

# Задание 3.
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(income)

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    def get_full_name(self):
        print(f'Сотрудник: {self.position} {self.name} {self.surname}')
    def get_total_incom(self):
        total_incom = self._income['оклад'] + self._income['премия']
        print(f'Доход сотрудника: {total_incom}')

w_1 = Position('Иван', 'Петров', 'Директор', [('оклад', 40000), ('премия', 20000)])
w_1.get_full_name()
w_1.get_total_incom()
w_2 = Position('Петр', 'Иванов', 'Заместитель директора', [('оклад', 30000), ('премия', 10000)])
w_2.get_full_name()
w_2.get_total_incom()
print(w_1.name)
print(w_1.surname)
print(w_1.position)
print(w_1._income)

# Задание 4.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Car go')
    def stop(self):
        print('Car stop')
    def turn(self, direction):
        self.direction = direction
        print(f'Сar turned {self.direction}')
    def show_speed(self):
        print(f'Car speed {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f'Car speed {self.speed} and exceeded by {(self.speed - 60)}')
        else:
            print(f'Car speed {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f'Car speed {self.speed} and exceeded by {(self.speed - 40)}')
        else:
            print(f'Car speed {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

c_1 = TownCar(65, 'red', 'Lincoln', False)
c_2 = SportCar(120, 'blue', 'Nissan', False)
c_3 = WorkCar(40, 'black', 'Ford', False)
c_4 = PoliceCar(80, 'white', 'Mersedes', True)
print(c_1.speed, c_1.name, c_1.color, c_1.is_police)
c_1.go()
c_1.stop()
c_1.turn('right')
c_1.show_speed()
print(c_2.speed, c_2.name, c_2.color, c_2.is_police)
c_2.go()
c_2.stop()
c_2.turn('left')
c_2.show_speed()
print(c_3.speed, c_3.name, c_3.color, c_3.is_police)
c_3.go()
c_3.stop()
c_3.turn('left')
c_3.show_speed()
print(c_4.speed, c_4.name, c_4.color, c_4.is_police)
c_4.go()
c_4.stop()
c_4.turn('right')
c_4.show_speed()

# Задание 5.
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Для отрисовки используется {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Для отрисовки используется {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Для отрисовки используется {self.title}')

s_1 = Pen('шариковая ручка')
s_1.draw()
s_2 = Pencil('простой карандаш')
s_2.draw()
s_3 = Handle('маркер')
s_3.draw()