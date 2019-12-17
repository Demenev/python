
# Задание 1. script_salary.py
from sys import argv

script_name, working_time, rate_hour, bonus = argv
def salary_func ():
    salary = int(working_time) * int(rate_hour) + int(bonus)
    print("Имя скрипта: ", script_name)
    print("Заработная плата сотрудника составит: ", salary, " рублей")

salary_func()

# Задание 2.
my_list = [23, 45, 32, 30, 38, 45]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(my_list)
print(new_list)

# Задание 3.
print('Список чисел кратных 21: ', [i for i in range(20, 240) if i % 21 == 0])

# Задание 4.
my_list = [20, 30, 45, 20, 70, 65, 45, 56, 39, 80, 56]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
print(new_list)

# Задание 5.
from functools import reduce

def my_func(prev_e1, e1):
    return prev_e1 * e1
my_list = [i for i in range(100, 1001) if i%2 == 0]
print(f'Сформированный список {my_list}')
print(f'Произведение всех чисел списка {reduce(my_func, my_list)}')

# Задание 6а. script_number.py
from sys import argv
from itertools import count

script_name, initial_val, final_val = argv
print("Имя скрипта: ", script_name)
for i in count(int(initial_val)):
    if i > int(final_val):
        break
    print(i, end=" ")

# Задание 6б. script_list.py
from sys import argv
from itertools import cycle

script_name, number_iter = argv
print("Имя скрипта: ", script_name)
my_list = ["огонь", "воздух", "вода", "земля"]
iter = cycle(my_list)
a = 0
while a < int(number_iter):
    print(next(iter))
    a += 1

# Задание 7.
def fibo_gen():
    my_factorial = 1
    for i in range(1, 16):
        my_factorial = my_factorial * i
        yield my_factorial

a = 0
for i in fibo_gen():
    a += 1
    print(f'Факториал числа {a} равен {i}')


