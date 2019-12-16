# Задание 1.
def my_func(var1, var2):
    return var1 / var2

var1 = int(input('Ведите первое число '))
var2 = int(input('Введите второе число '))
while True:
    if var2 == 0:
        var2 = int(input('Введите число отличное от нуля '))
    else:
        break
print(f'Результат от деления двух чисел  {my_func(var1, var2):.4}')

# Задание 2.
def user_func(var_1, var_2, var_3, var_4, var_5, var_6):
    print(f'User: name - {var_1}, surname - {var_2}, birth year - {var_3}, city of residence - {var_4}, email - {var_5}, tel - {var_6}')

user_func(var_1 = 'Serg', var_2 = 'Ivanov', var_3 = 1980, var_4 = 'Moscow', var_5 = 'geek@mail.com', var_6 = '6-89-78')

# Задание 3.
def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    my_list.pop(0)
    return sum(my_list)

sum_max = my_func(-5, 45, -10)
print(f'Суммa максимальных аргуметов равна {sum_max}')

# Задание 4.
def my_func(x, y):
    return x**y
def new_func(x, y):
    a = 1
    for i in range(-y):
        a = a * (1 / x)
    return a

x = int(input('Введите положительное число '))
y = int(input('Введите отрицательное число '))
print(f'Число {x} в степни {y} - {my_func(x, y)}')
print(f'Число {x} в степни {y} - {new_func(x, y)}')

# Задание 5.
def sum_func():
    final_sum = 0
    while True:
        sum = 0
        numbers_list = input(('Введите числа через пробел или "q" для выхода ')).split()
        if numbers_list.count('q') == 0:
            for i in range(len(numbers_list)):
                sum = sum + int(numbers_list[i])
            final_sum = final_sum + sum
            print(f'Сумма чисел введенной строки равна {sum}')
        else:
            for i in range(numbers_list.index('q')):
                sum = sum + int(numbers_list[i])
            final_sum = final_sum + sum
            print(f'Сумма чисел введенной строки равна {sum}')
            break
    print(f'Сумма всех введенных чисел равна {final_sum}')

sum_func()

# Задание 6.
int_func = lambda d: d.title()
a = int(input('Введите количество необходимых слов '))
m_list = []
for i in range(a):
    m = input('Введите слово латинскими в нижнем регистре ')
    m_list.append(m)
d = " ".join(m_list)
print(int_func(d))