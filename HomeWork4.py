#  Напишите цикл, который выводит на экран и удаляет с конца последний
# первый символ строки, пока она не станет пустой.

a = 'Hello world'
while len(a):
    a = a[0:(len(a)-1)]
    print(a)

#  Проверить тип всех элементов списка. Если тип элемента не строковый,
# преобразовать его в строку. Попробуйте не просто преобразоват
# ь, а ещё и
# перезаписать этот элемент, преобразованный в строку

a = ['Hello world!',3,4.0,9]
for se in range(len(a)):
    if type(se) != str:
        a[se] = str(a[se])
        print(a[se])
    else:
        print(a[se])

#  А как прочитать построчно с помощью цикла for? И, например, вывести на
# каждой итерации “строка из файла” + “!” (Разберитесь почему так много
# переводов строки там, где вы не ожидали и пофиксите эту багу)


input_file = open("E:\\work\\python_script\\python\\test.txt")
read = input_file.readline()
for line in input_file:
    print(line.rstrip() + '!')

# Задание 1
# Пользователь вводит число. (Проверка на входные данные должна быть, и
# человек должен вводить значения пока не введёт правильно)
# Определите знак числа и выведите его не экран.

while True:
    s = input('введите число: ')
    print(s.isalpha())
    if s.isalpha() == False :
        m = float(s)
        if m == 0:
            print('ноль:' , m )
        elif m > 0:
            print('положительное:', m)
        elif m < 0:
            print('отрицательное:', m)
        break
    else:
            print('это не число')


# Задание 2
# Даны два целых числа A и В. Выведите все числа от A до B включительно, в
# порядке возрастания, если A < B, или в порядке убывания в противном случае.

a = 50
b = 10
if b > a:
    for a in range(a,b+1):
        print(a)
else:
    for a in range(a,b-1,-1):
        print(a)


# Задание 3
# У вас есть список чисел. Подсчитайте, сколько из них равны нулю и сколько
# отрицательных, и сколько положительных, и выведите эти количества.

s_0 = 0
s_minus = 0
s_plus = 0
a = [4,4,6,0,-7,0]
for m in a:
    if m == 0:
        s_0 = s_0 +1
    elif m < 0:
        s_minus = s_minus +1
    elif m > 0:
        s_plus = s_plus +1
print('нулей - ',s_0,'минусовых значений - ',s_minus, 'положительных - ',s_plus)


# Задание 4
# Пользователь вводит целое число. (Проверка на входные данные должна быть, и
# человек должен вводить значения пока не введет правильно)
# Вычислите факториал числа. Факториал – это n! = 1*2*3*…*n


while True:
    fac = 1
    i = 0
    s = input('введите число: ')
    if s.isdigit() == True:
        s = int(s)
        while i < s:
            i += 1
            fac = fac * i
    print('Факториал:' , fac )
    break


# Задание 5
# У вас есть список целых чисел. Выведите все элементы списка, которые делятся
# на 3.

a = [4,4,6,0,7,9]
for m in a:
    if m / 3 == m // 3:
        print(m)


# Задание 6
# Посчитать сколько раз встречается слово «we» в текстовом файле (не зависимо
# от регистра символов).
# Extra уровень: имя файла в котором надо считать получите из аргумента
# командной строки

import sys
import re
#files = str(sys.argv[1])
files = 'test.txt'
files_full = 'E:\\work\\python_script\\python\\'+ files
input_file = open(files_full)
m = input_file.read()
m = m.lower()
parr = re.compile('we')
print(len(parr.findall(m)))
input_file.close()

# Задание 7
# Во входном файле есть два целых положительных числа среди другого текста
# (все слова и цифры окружают пробелы, но до пробела могут идти знак точки или
# запятой). Найдите их и выведите в выходной файл их сумму.
# Extra уровень: имя файла в котором надо считать получите из аргумента
# командной строки


summ = 0
import sys
import re
#files = str(sys.argv[1])
files = 'test.txt'
files_full = 'E:\\work\\python_script\\python\\'+ files
input_file = open(files_full)
m = input_file.read()
s = re.findall(r'\w+',m)
for data in s:
    if data.isalpha() == False :
        data = float(data)
        summ = summ + int(data)
my_file = open("E:\\work\\python_script\\python\\rezultat.txt", "w")
my_file.write(str(summ))
my_file.close()
print(summ)
input_file.close()


# Задание 8
# У вас есть список чисел и строк. Выделите элементы с числами и отдельно со
# строками в два отдельных списка. Порядок должен сохраняться.

summ = 0
import re
datanum = []
datastr = []
files = 'test.txt'
files_full = 'E:\\work\\python_script\\python\\'+ files
input_file = open(files_full)
m = input_file.read()
s = re.findall(r'\w+',m)
for data in s:
    if data.isalpha() == False :
        datanum.append(data) # или print(data)
for data in s:
    if data.isalpha() == True :
        datastr.append(data) # или print(data)
print(datanum,datastr)
input_file.close()

# Задание 9 (доп. уровень. Тут вам нужно поискать как делать то, что мы не учили
# в стандартных библиотеках)
# Даны два натуральных числа n и m из командной строки. Если одно из них
# делится на другое нацело, выведите 1, иначе выведите любое другое целое
# число из диапазона 1 до 1000 включая.

# import random
# import sys
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# if num1 / num2 == num1 // num2:
#     s = 1
# else:
#     s = random.randint(1,1000)
# print(s)
