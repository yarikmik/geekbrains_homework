import random

generate = [i for i in range(1, 91)]
card = [['--', '--', '--', '--'], ['--', '--', '--', '--'], ['--', '--', '--', '--']]

for i in card:
    count = 1
    while count <= 5:
        i.append(generate.pop(random.randint(0, len(generate)-1)))
        count += 1
    random.shuffle(i)

print(generate)
print(card)
