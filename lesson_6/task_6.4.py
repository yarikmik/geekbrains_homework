"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
import random

class Car:
    def __init__(self, speed, color, name, is_police):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name
        self.is_police = is_police

    def go(self):
        print('Машина начала движение')

    def stop(self):
        print('Машина остановлена')

    def turn(self):
        if random.random() < 0.5:
            print('Машина повернула на право')
        else:
            print('Машина повернула на лево')

    def show_speed(self):
        print('Скорость - ', self.car_speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.car_speed > 60:
            print(f'Скорость выше 60, текущая скорость - {self.car_speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.car_speed > 40:
            print(f'Скорость выше 40, текущая скорость - {self.car_speed}')


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            print('Это полицейская машина')


car1 = WorkCar(55, 'Зеленая', 'Тойота', False)
print(car1.car_name, car1.car_color)
car1.go()
car1.turn()
car1.show_speed()
car1.stop()

car2 = PoliceCar(120, 'Синий', 'автозак', True)
print('\n', car2.car_name, car2.car_color)
car2.go()
car2.turn()
car2.show_speed()
car2.stop()
car2.police()

car3 = TownCar(120, 'Красная', 'Газель', False)
print('\n', car3.car_name, car3.car_color)
car3.go()
car3.turn()
car3.show_speed()
car3.stop()

