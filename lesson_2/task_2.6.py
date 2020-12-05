"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с
параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""
tuples_list = []

count = 1
while count <= 3:
    product = input(f'Введите название {count}-го товара: ')
    price = input(f'Введите цену {count}-го товара - "{product}": ')
    number = input(f'Введите колличество {count}-го товара - "{product}": ')
    unit = input(f'Введите единицу измерения {count}-го товара - "{product}": ')
    product_tuple = (count, {'название': product, 'цена': price, 'количество': number, 'eд': unit})
    tuples_list.append(product_tuple)
    count += 1
# print(tuples_list)

result_dict = {}
parametres = []
parametres2 = []
parametres3 = []
parametres4 = []

for position in tuples_list:
    for key, value in position[1].items():

        if key == 'название':
            parametres.append(value)
            result_dict[key] = parametres
        if key == 'цена':
            parametres2.append(value)
            result_dict[key] = parametres2
        if key == 'количество':
            parametres3.append(value)
            result_dict[key] = parametres3
        if key == 'eд':
            parametres4.append(value)
            result_dict[key] = parametres4

print(result_dict)
