"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

"""
import json

def calculate_firms(file):
    result = []
    all_firms = {}
    average_profit = {}
    count_pf = 0
    profit_summ = 0

    txt = file.readlines()
    for s in txt:
        all_firms[s.split()[0]] = int(s.split()[2]) - int(s.split()[3])
        if int(s.split()[2]) > int(s.split()[3]):
            count_pf += 1
            profit_summ += int(s.split()[2]) - int(s.split()[3])
    # average_profit['average_profit'] = round(sum([v for v in profit_firms.values()]) / count_pf, 2)
    average_profit['average_profit'] = round(profit_summ/count_pf, 2)
    result.append(all_firms)
    result.append(average_profit)
    file.seek(0)
    return result


with open('task_5.7_1.txt') as file_1, open('task_5.7_2.txt', 'w') as file_2 :
    print(calculate_firms(file_1))
    print(json.dump(calculate_firms(file_1), file_2))

