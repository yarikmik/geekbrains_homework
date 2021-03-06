"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12,
количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""

class Cell:
    def __init__(self, value):
        self.mesh = value

    def __add__(self, other):
        """сложение"""
        return Cell(self.mesh + other.mesh)

    def __sub__(self, other):
        """вычитание"""
        if self.mesh < other.mesh:
            return f'Ошибка, разность меньше нуля'
        return Cell(self.mesh - other.mesh)


    def __mul__(self, other):
        """умножение"""
        return Cell(self.mesh * other.mesh)

    def __truediv__(self, other):
        """деление"""
        return Cell(self.mesh // other.mesh)

    def __str__(self):
        return f"Клетка с {self.mesh} ячейками "

    def make_order(self, divider):
        self.divider = divider
        st = self.mesh//self.divider
        result = ''
        while st != 0:
            result += '*' * self.divider + '/n'
            st -= 1
        result += ('*' * (self.mesh - self.mesh//self.divider * self.divider ))
        return print(result)


c1 = Cell(16)
c2 = Cell(15)
c3 = Cell(35)
c4 = Cell(4)
print('сложение - ', c1 + c2 + c3)
print('вычитание - ', c1 - c2 - c3)
print('умножение - ', c1 * c2 * c3)
print('умножение - ', c2 / c3, '\n')

c5 = c1 + c2
print(c5)
c6 = c3 - c2
print(c6)
c9 = c2 - c3
print(c9)
c7 = c1 * c2
print(c7)
c8 = c3 / c2
print(c8, '\n')

c10 = Cell(38)
c10.make_order(12)

