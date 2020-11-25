"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['   '.join([str(i) for i in a]) for a in self.matrix]) + '\n'

    def __add__(self, other):
        if len(self.matrix) != len(other):
            return print('Массивы разной длинны')
        for m1_str in self.matrix:
            for m2_str in other:
                if len(m1_str) != len(m2_str):
                    return print('В строках разное колличество значений')

        # Сложение массивов:
        summ_arr = []
        for i in range(len(self.matrix)):
            summ = []
            for s in range(len(self.matrix[i])):
                summ.append(self.matrix[i][s] + other[i][s])
            summ_arr.append(summ)
        return Matrix(summ_arr)


matrix1 = Matrix([[3, 3, 5], [2, 5, 7], [1, 3, 0]])
matrix2 = Matrix([[1, 1, 1], [2, 2, 2], [2, 2]])
matrix3 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
list1 = [[0, 1, 1], [2, 1, 2]]
list2 = [[4, 3, 2], [1, 0, 0], [6, 2, 1]]
print(matrix1)
print(matrix2)
print(matrix3)

print(f'Неудачное сложение: {matrix1 + matrix2.matrix}\n')
print(f'Неудачное сложение: {matrix1 + list1}\n')
print(f'Удачное сложение: \n{matrix1 + matrix3.matrix + list2}\n')




