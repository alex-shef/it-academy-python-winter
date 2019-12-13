# 1. Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество L товара.
# Посчитайте общую цену в рублях и копейках за L товаров.

M = int(input("1. Введите кол-во рублей: ", ))
N = int(input("Введите кол-во копеек: ", ))
L = int(input("Введите кол-во товара: ", ))
print("Общая сумма:", M * L + (N * L) // 100, "рублей",
      (N * L) % 100, "копеек")

# 2. https://py.checkio.org
# Say Hi
# В этой миссии вы должны написать функцию,
# которая представит человека по переданным параметрам.
# Входные данные: Два аргумента строка(str) и положительное число(int)
# Output: Строка(str).


def say_hi(name, age):
    age = str(age)
    return "Hi. My name is " + name + " and I'm " + age + " years old"


# https://acmp.ru/index.asp?main=task&id_task=18
#  Факториал
# Требуется вычислить факториал целого числа N.

f = 1
N = int(input("2. Введите целое число для факториала: "))
for i in range(1, N + 1):
    f *= i
print("факториал=", f)

# https://acmp.ru/index.asp?main=task&id_task=384
# Числа Фибоначчи - 3
# Требуется найти наибольший общий делитель двух чисел Фибоначчи.

i = int(input("2. Введите индексы чисел Фибоначчи: ", ))
j = int(input("Введите индексы чисел Фибоначчи: ", ))


def fibo(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return fibo(x - 1) + fibo(x - 2)


a = fibo(i)
b = fibo(j)
print("Fi=", a, "Fj=", b)

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("НОД=", a)

# 3. Найти самое длинное слово в введенном предложении.
# **: учтите что в предложении есть знаки препинания.

a = input('3. Введите предложение: ', )
a = a.replace(',', '')
a = a.replace('.', '')
a = a.replace('—', '')
a = a.replace(':', '')
lst = a.split()
maxlen = lst[1]
for elem in lst:
    if len(elem) > len(maxlen):
        maxlen = elem
print("Самое длинное слово:", maxlen)

# 4. Вводится строка.
# Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

a = input('4. Введите строку: ', )
a = a.replace(' ', '')
lst = []
for i in a:
    if i not in lst:
        lst.append(i)
print(''.join(lst))

# 5. Посчитать количество строчных (маленьких)
# и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

string = input('5. Введите строку: ', )
lower = upper = 0
for i in string:
    if 'a' <= i <= 'z':
        lower += 1
    elif 'A' <= i <= 'Z':
        upper += 1
print("Кол-во английских букв, строчных:", lower, "прописных:", upper)

# -Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится

n = int(input("Введите индекс числа Фибоначчи: ", ))
f = 0
f0 = 0
f1 = 1
if n == 1:
    f = 1
else:
    for i in range(1, n):
        f = f1 + f0
        f0 = f1
        f1 = f
print(f)

# - Определите, является ли число палиндромом
# (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку)

n = int(input("Проверка числа на палиндром: ", ))
s = 0
m = n
while m > 0:
    s = 10 * s + m % 10
    m //= 10
if s == n:
    print('палиндром')
