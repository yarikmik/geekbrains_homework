import random


class LotoCard:
    def __init__(self, name):
        self.name = name
        self.generate = [i for i in range(1, 91)]
        self.card = [['--', '--', '--', '--'], ['--', '--', '--', '--'], ['--', '--', '--', '--']]
        for i in self.card:
            count = 1
            while count <= 5:
                i.append(self.generate.pop(random.randint(0, len(self.generate) - 1)))
                count += 1
            random.shuffle(i)

    def __str__(self):
        text_card = f'{self.name}: \n' + '\n'.join(['   '.join([str(i) for i in a]) for a in self.card]) + '\n'
        return text_card

class LotoGame:
    def __init__(self, name1, name2):
        self.player1 = name1
        self.player2 = name2
        self.generate = [i for i in range(1, 91)]

    def start_game(self):
        count = 1
        while count < len(self.generate):
            print(self.generate.pop(random.randint(0, len(self.generate) - 1)))
            count += 1




human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

print(human_player)
print(computer_player)
game = LotoGame(human_player, computer_player)
game.start_game()
