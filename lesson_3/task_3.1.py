"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(value_1, value_2):
    try:
        return value_1 / value_2
    except ZeroDivisionError:
        print('Нельзя делить на ноль')

while True:
    try:
        x = int(input('Введите делимое: '))
        y = int(input('Введите делитель: '))
        break
    except ValueError:
        print('Введите числа')

print(f'{x}/{y} =', my_func(x, y))
