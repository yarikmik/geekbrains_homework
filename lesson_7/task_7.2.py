"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    textile_summ = []

    def __init__(self, name, x):
        self.name = name
        self.value = x
        # print(name)

    @abstractmethod
    def coat_calculate(self):
        pass

    @abstractmethod
    def suit_calculate(self):
        pass


class SuitAndCoat(Clothes):

    def coat_calculate(self):
        self._V = self.value
        self._coat_textile = self._V / 6.5 + 0.5
        self.textile_summ.append(self._coat_textile)
        return print(f'Для "{self.name}" необходимо {round(self._coat_textile, 1)}м ткани')

    def suit_calculate(self):
        self._H = self.value
        self._suit_textile = 2 * self._H + 0.3
        self.textile_summ.append(self._suit_textile)
        return print(f'Для "{self.name}" необходимо {round(self._suit_textile, 1)}м ткани')


class Textile():

    @property
    def textile_calculate(self):
        return print('необходимо ткани всего - ', round(sum(SuitAndCoat.textile_summ), 1))


r = Textile()
cl = SuitAndCoat('Серое пальто', 10)
cl.coat_calculate()
su = SuitAndCoat('Строгий костюм', 20)
su.suit_calculate()

r.textile_calculate

cl2 = SuitAndCoat('Синее пальто', 11)
cl2.coat_calculate()

r.textile_calculate
