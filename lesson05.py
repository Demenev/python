# Задание 1.
my_f = open('my_file.txt', 'w')
while True:
    my_str = input('Введите строку ')
    my_f.write(my_str + '\n')
    if my_str == "":
        break
my_f.close()

# Задание 2.
my_f = open(r"C:\Users\Сергей\Documents\GitHub\python\my_file.txt", 'r')
a = 0
for line in my_f:
    print(line)
    print('Количество слов в строке - ', len(line.split()))
    a += 1
print(f'Количество строк в файле - {a}')
my_f.close()

# Задание 3.
my_f = open(r"C:\Users\Сергей\Documents\GitHub\python\my_file_1.txt", 'r')
my_dict = dict([line.split() for line in my_f])
print('Работники, имеющие оклад меньше 20000:')
a = 0
for key, value in my_dict.items():
    a = a + int(value)
    if int(value) < 20000:
        print(f'{key} - {value}')
print('Средний доход всех сотрудников составляет - ', a/len(my_dict))
my_f.close()

# Задание 4.
my_f = open(r"C:\Users\Сергей\Documents\GitHub\python\my_file_2.txt", 'r')
out_f = open('my_new_file.txt', 'w')
my_list = ['Один', 'Два', 'Три', 'Четыре']
i = 0
for line in my_f:
    new_list = line.strip().split(' - ')
    new_list[0] = my_list[i]
    print(' - '.join(new_list), file=out_f)
    i +=1
my_f.close()
out_f.close()

# Задание 5.
with open('number_file.txt', 'w') as number_f:
    number_f.write(input('Введите числа через пробел '))
with open('number_file.txt', 'r+') as number_f:
    my_lyst = number_f.readline().split()
    number_sum = 0
    for i in my_lyst:
        number_sum = number_sum + int(i)
    print(f'Сумма чисел в файле number_file.txt равна {number_sum}')

# Задание 6.
with open("curriculum.txt", 'r') as my_f:
    my_dict = {}
    for line in my_f:
        my_list = line.split()
        key = my_list[0]
        study_hours = my_list[1:]
        my_dict[key] = 0
        for i in study_hours:
            try:
                my_dict[key] += int(i)
            except ValueError:
                pass
print(my_dict)

# Задание 7.
import json
with open('my_file_7.txt', 'r') as my_f:
    my_dict = {}
    company_list = []
    average_profit = 0
    i = 0
    for line in my_f:
        my_list = line.strip().split()
        key = my_list[0]
        my_dict[key] = int(my_list[-2]) - int(my_list[-1])
        if my_dict[key] >= 0:
            average_profit = average_profit + my_dict[key]
            i +=1
    average = dict(average_profit=int(average_profit/i))
    company_list.append(my_dict)
    company_list.append(average)
    print(company_list)
with open('my_file_7.json', 'w') as write_f:
    json.dump(company_list, write_f)