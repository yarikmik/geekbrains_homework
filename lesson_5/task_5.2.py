"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('task_5.2.txt') as file:
    txt = file.readlines()

str_count = len(txt)
for num, st in enumerate(txt, 1):
    print(f'Слов в {num}-й строке = {len(st.split())}')

print(f'Всего строк - {str_count}')