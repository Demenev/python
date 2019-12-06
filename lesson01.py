#переменные
number = 35
name = "Serg"
print(number, name)
user_name = input('Введите ваше имя ')
user_age = input('Ваш возраст ')
print(f'Пользователя зовут {user_name}, его возраст {user_age}')

#перевод времени
sec = int(input('Введите время в секундах '))
h = sec//3600
m = (sec//60)%60
s = sec%60
if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
if s < 10:
    s = '0' + str(s)
print(f'Время {h}:{m}:{s}')

#сложение n+nn+nnn
n = input('Введите число от 1 до 9 ')
nn = n + n
nnn = nn + n
summ = int(n) + int(nn) + int(nnn)
print(n,'+',nn,'+',nnn,'=', summ)

#наибольшая цифра в числе
a = int(input('Введите целое положительное число '))
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print('Максимальная цифра в числе', m)

#выручка
rev_comp = int(input('Введите выручку фирмы '))
cost_comp = int(input('Введите издержки фирмы '))
if rev_comp < cost_comp:
    print('Фирма банкрот')
elif rev_comp == cost_comp:
    print('У фирмы нет прибыли')
else:
    rent = (rev_comp - cost_comp)/rev_comp*100
    numbers = int(input('Количество сотрудников в фирме '))
    profit_pers = (rev_comp - cost_comp)/numbers
    print(f'Фирма приносит прибыль. Рентабельность {rent:.2f} процентов. Прибыль на одного работника {profit_pers:.2f}')

#спортсмен
a = int(input('Ведите результат спортсмена в первый день '))
b = int(input('Введите конечный результат спортсмена '))
i = 1
print(f'{i}-й день: {a:.2f} км')
while True:
    if a > b:
        break
    else:
        a = a + a*0.1
        i +=1
        print(f'{i}-й день: {a:.2f} км')
print(f'на {i}-й день спортсмен достиг результата - не менее {b} км') 