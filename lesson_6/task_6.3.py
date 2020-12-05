"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    _income = {}
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus

class Position(Worker):

    def get_full_name(self):
        print('{}, {}'.format(self.surname, self.name))


    def get_total_income(self):
        _total = 0
        for key, value in Position._income.items():
            _total += value
        print(_total)


wizard = Position('Воланд', 'ДеМорт', 'главный по палочкам', 50000, 5600)

wizard.get_full_name()
wizard.get_total_income()
print(wizard.position, '\n')

wizard = Position('Гарри', 'Поттер', 'специалист по притягиванию неприятностей', 30000, 1600)
wizard.get_full_name()
wizard.get_total_income()
print(wizard.position, '\n')

