"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

own_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def convert_file(file):
    new_txt = []
    txt = file.readlines()
    for i in txt:
        st = i.split()  # Делим каждую строку
        if st[0] in own_dict:  # Первый элемент проверяем есть ли в словаре
            deleted = st.pop(0)
            st.insert(0, own_dict[deleted])  # Первый элемент вырезаем и меняем на значение соответствующего ключа
        new_txt.append(' '.join(st))
    return new_txt


with open('task_5.4_1.txt') as file_1, open('task_5.4_2.txt', 'w') as file_2 :
    for s in convert_file(file_1):
        file_2.write(s + '\n')
