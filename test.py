import random

def calculate_loto_card(card, loto_chip):
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

generate = [i for i in range(1, 91)]
card = [['--', '--', '--', '--'], ['--', '--', '--', '--'], ['--', '--', '--', '--']]

for i in card:
    count = 1
    while count <= 5:
        i.append(generate.pop(random.randint(0, len(generate)-1)))
        count += 1
    random.shuffle(i)

# print(generate)
print(card)
print(calculate_loto_card(card, 88))
print(card)
print(amount_numbers(card))
