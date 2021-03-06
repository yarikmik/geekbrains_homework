"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def calculate(user_input):
    summ = 0
    for i in user_input.split():
        if i.upper() == 'Q':
            return summ
        summ += int(i)

    return summ


answer = 0

while True:
    user_input = input('Введите ряд чисел через пробел, для выхода введите Q: ')
    answer += calculate(user_input)
    print(f'Cумма текущей последовательности = {calculate(user_input)}, общая сумма = {answer}')
    if 'Q' in user_input.upper():
        print('Ввод завершен')
        break

print('Итоговая сумма = ', answer)
