# Задание 1.
list_user = ['дерево', 3, 4.05, True, ('восток', 'юг')]
for i in list_user:
    print(i, type(i))

# Задание 2.
a = []
b = int(input('Введите количество элементов списка '))
for i in range(b):
    el = input('Введите элемент списка ')
    a.append(el)
print(a)
i = 0
while i < (b-1):
    a[i], a[i + 1] = a[i + 1], a[i]
    i = i + 2
print(a)

# Задание 3.
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
month = int(input('Введите номер месяца в интервале от 1 до 12 '))
if month >= 3 and month < 6:
    print(f'Время года - весна, {month} месяц года - {month_list[month - 1]}')
    print(f'Время года - весна, {month} месяц года - {month_dict.get(month)}')
elif month >= 6 and month < 9:
    print(f'Время года - лето, {month} месяц года - {month_list[month - 1]}')
    print(f'Время года - лето, {month} месяц года - {month_dict.get(month)}')
elif month >= 9 and month < 12:
    print(f'Время года - зима, {month} месяц года - {month_list[month - 1]}')
    print(f'Время года - зима, {month} месяц года - {month_dict.get(month)}')
else:
    print(f'Время года - зима, {month} месяц года - {month_list[month - 1]}')
    print(f'Время года - зима, {month} месяц года - {month_dict.get(month)}')

# Задание 4.
my_str = 'продемонстрировать квадратичную функцию'
my_list = my_str.split()
for ind, el in enumerate(my_list, 1):
    print(ind, el[:10])

# Задание 5.
my_list = [5, 5, 4, 3, 2]
while True:
    b = len(my_list)
    number = int(input('Введите положительное число '))
    for i in range(b-1):
        if number == my_list[i]:
            my_list.insert(i + my_list.count(number), number)
            break
        elif number > my_list[i]:
            my_list.insert(i,number)
            break
        elif number <= min(my_list):
            my_list.append(number)
            break
    print(my_list)

# Задание 6.
a = int(input('Введите количество товара '))
goods_list = []
title_list = []
price_list = []
quantity_list = []
n = 1
while n <=a:
    goods_dict = dict({'название': input('Ведите название товара '),
                'цена': input('Введите цену товара '),
                'количество': input('Введите количество товара '),
                'ед.': input('Введите единицу измерения ')})
    goods_list.append((n, goods_dict))
    n +=1
    title_list.append(goods_dict.get('название'))
    price_list.append(goods_dict.get('цена'))
    quantity_list.append(goods_dict.get('количество'))
analitics = dict({'название': title_list, 'цена': price_list, 'количество': quantity_list, 'ед.': goods_dict.get('ед.')})
print(goods_list)
print(analitics)