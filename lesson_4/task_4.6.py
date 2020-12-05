"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.

"""
from itertools import count, cycle
import time

# скрипт а:
start_number = int(input('Введите число: '))
for i in count(start_number):
    if i > 10:
        break
    else:
        print(i)

# скрипт б:
task_list = ['up', 'down', 'left', 'right']
c = 0
for i in cycle(task_list):

    if c < 10:
        time.sleep(0.5)
        print(i)
        c += 1
    else:
        break


