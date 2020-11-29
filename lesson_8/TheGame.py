import random


def calculate_loto_card(card, loto_chip):
    '''
    Обрабатывает лотерейную карточку, выпавшее значение боченка заменяется в карточке на хх
    :param card: лотерейная карточка
    :param loto_chip: выпавший боченок
    :return: False/True
    '''
    result = False
    for string in card:
        for i in range(len(string)):
            if string[i] == loto_chip:
                string[i] = 'xx'
                result = True
    return result


def amount_numbers(card):
    '''
    Возвращает колличество оставшихся номеров в карточке
    '''
    count = 0
    for string in card:
        for i in string:
            if str(i).isdigit():
                count += 1
    return count


def number_correct(n):
    '''
    Для красоты вывода, добавляет пробел перед одиночным символом, что бы табличка не плыла
    '''
    if len(str(n)) < 2:
        return ' ' + str(n)
    else:
        return str(n)


class LotoCard:
    def __init__(self, name):
        self.name = name
        self.generate = [i for i in range(1, 91)]
        self.card = [['--', '--', '--', '--'],
                     ['--', '--', '--', '--'],
                     ['--', '--', '--', '--']]  # заготовка для карточек
        for i in self.card:
            count = 1
            while count <= 5:
                # заполнение карточки рандомными значениями:
                i.append(self.generate.pop(random.randint(0, len(self.generate) - 1)))
                count += 1
            # Перемешивание значений в строке карточки:
            random.shuffle(i)

    def __str__(self):
        # Текстовый выод карточки на экран
        text_card = f'{self.name}: \n' + '\n'.join(
            ['   '.join([number_correct(i) for i in a]) for a in self.card]) + '\n'
        return text_card


class InputUser:
    """Проверка пользовательского ввода"""

    def __init__(self, user_input=None):
        if not user_input:
            while True:
                self.user_input = input('Зачеркнуть цифру? (y/n)\n')
                if self.user_input == 'n' or self.user_input == 'y':
                    break
                else:
                    print('Возможны только значения y или n\n')


class LotoGame:
    """Класс, описывающий игру"""

    def __init__(self, name1, name2):
        self.player1 = name1
        self.player2 = name2
        self.generate = [i for i in range(1, 91)]

    def start_game(self):
        count = 1
        while count < 90:
            loto_chip = self.generate.pop(random.randint(0, len(self.generate) - 1))
            print('Выпал боченок - ', loto_chip, f'(Осталось - {len(self.generate)})')
            count += 1
            print(human_player)
            print(computer_player)
            user_answer = InputUser()  # пользовательский ввод
            if calculate_loto_card(human_player.card, loto_chip):
                if user_answer.user_input != 'y':
                    print('Вы проиграли, такой боченок есть в карточке')
                    break
            else:
                if user_answer.user_input != 'n':
                    print('Вы проиграли, такого боченка нет в карточке')
                    break
            calculate_loto_card(computer_player.card, loto_chip)

            # подсчет промежуточных результатов:
            print(f'Номеров осталось у {human_player.name} ', amount_numbers(human_player.card))
            print(f'Номеров осталось у {computer_player.name} ', amount_numbers(computer_player.card))

            # Условие победы:
            if amount_numbers(human_player.card) == 0:
                print('Победил - ', human_player.name)
                break
            elif amount_numbers(computer_player.card) == 0:
                print('Победил - ', computer_player.name)
                break


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = LotoGame(human_player, computer_player)
game.start_game()
