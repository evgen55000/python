# Задания 0 (тем, кто не доделал в классе)
# Есть список целых положительных чисел. Проверяем, есть ли в этом списке два
# равных соседних числа. Создаём новый список без повторяющихся равных соседей

a = [3,5,3,6,6,7,8]
b = []
for sp in range(0,len(a)):
  #  print (a[sp])
    if a[sp-1] == a[sp]:
        continue
    b.append(a[sp])
print(b)


# Задание 1
# Считываем текст из файла. Посчитываем сколько в нем используется слов
# (уникальных). Не учитывать знаки пунктуации и регистр символов (слово с
# большой буквы и с маленькой – это одно и то же слово)
#  Выведите их на экран
#  Выведите количество таких слов

unic = set()
in_file = open("E:\\work\\python_script\\work\\test.txt", 'r')
read = in_file.read()
read = read.lower()
read = read.split()
for file in read:
    file = file.rstrip()
    unic.add(file)
print(unic)
print(len(unic))

# Задание 2
# Считываем слова из 2-х файлов. Выведите слова, которые используются в обоих
# файлах
# Выведите слова, которые используются в первом файле, но не используются во втором

unic = set()
unic2 = set()
in_file = open("E:\\work\\python_script\\work\\test.txt", 'r')
in_file2 = open("E:\\work\\python_script\\work\\test2.txt", 'r')
read = in_file.read()
read = read.lower()
read = read.split()
for file in read:
    file = file.rstrip()
    unic.add(file)
read2 = in_file2.read()
read2 = read2.lower()
read2 = read2.split()
for file2 in read2:
    file2 = file2.rstrip()
    unic2.add(file2)
#print(unic)
#print(unic2)
print(unic & unic2)


# Задание 3
# Записывает в новый файл все слова из файла с текстом в алфавитном порядке.
# Каждое слово на новой строке.

book = []
in_file = open("E:\\work\\python_script\\work\\test.txt", 'r')
out_file = open("E:\\work\\python_script\\work\\test3.txt", 'w')
read = in_file.read()
read = read.split()
for file in read:
    file = file.rstrip()
    book.append(file)
for out_book in book:
    print(out_book)
    print(out_book  ,file = out_file)

# Задание 4
# Создайте словарь departments, и наполните его данными, которые бы отражали
# количество работников в десяти разных отделах (ключи - это названия отделов)  (просто литералом словаря).
# 1. Выведите пользователю названия всех отделов, как подсказку пользователю для следующего пункта-подзадания.
# 2. Пусть пользователь вводит название отдела, а ему программа отвечает сколько человек в отделе.
# 3. Если пользователь введет слово “all”, выведите ему сколько всего работает людей во всех отделах.

import re
departments = {'маркетинг': 10, 'ит': 7, 'реклама': 6, 'бугалтерия': 20, 'охрана': 3, 'продавцы': 30, 'тех. отдел': 3, 'администратор': 3, 'ит_3': 7, 'охрана2': 3}
for name_dep in departments:
    print(name_dep)
while True:
     a = input('Введите название отдела: ')
     a = a.lower()
     if  re.findall(r' ', a):
        print('вы что то не то ввели')
        continue
     else:
        if a == 'all':
            for name_dep, count in departments.items():
                print(name_dep, count)
        elif departments.get(a) == None:
            print('нет такого отдела')
        else:
            print(a, ' - ', departments.get(a), 'чел.')


# Задание 4*
# Имеем тот же словарь departments
# 4. Дайте возможность пользователю менять количество работников в отделе. Пользователь вводит название отдела, а потом новое количество
# работников. Поменяйте это значение в исходном словаре. А теперь для проверки выведите все содержимое словаря.
# 5. Дайте возможность пользователю создать новый отдел. Сначала ввести название нового отдела, а потом ввести количество работников в этом отделе

import re
departments = {'маркетинг': 10, 'ит': 7, 'реклама': 6, 'бугалтерия': 20, 'охрана': 3, 'продавцы': 30, 'тех. отдел': 3, 'администратор': 3, 'ит_3': 7, 'охрана2': 3}
for name_dep in departments:
    print(name_dep)
while True:
     a = input('Введите название отдела: ')
     a = a.lower()
     if  re.findall(r' ', a):
        print('вы что то не то ввели')
        continue
     else:
        if departments.get(a) == None:
            print('нет такого отдела')
            add_dep = input('хотите добавить новый отдел? :')
            if add_dep == 'да':
                dep_new = input('введите новый отдел: ')
                count = int(input('введите количество сотрудников в этом отделе: '))
                departments.update({dep_new: count})
                for name_dep, count in departments.items():
                    print(name_dep, count)
            else: continue
        else:
            count = int(input('введите количество сотрудников в этом отделе: '))
            departments.update({a:count})
            for name_dep, count in departments.items():
                print(name_dep, count)

# Задание 5 (доп.)
# Считываем текст из файла. Посчитываем раз сколько в нем используется каждое
# слово. Выводим на экран:
# Слово1: X раз
# Слово2: Y раз
# ...
# Подсказка: используйте словарь. Множества для этого задания не нужны


book = []
in_file = open("E:\\work\\python_script\\work\\test.txt", 'r')
read = in_file.read()
read = read.split()
for file in read:
    file = file.rstrip()
    book.append(file)
for book_coun in book:
    print(book_coun, book.count(book_coun))

# Задание 6 (доп.)
# Файл имеет такой вид: Фамилия Имя Отдел Зарплата (В первой строке заголовки колонок)
#  Посчитайте сколько отделов на фирме
#  Определите максимальную зарплату
#  Определите максимальную зарплату в каждом отделе
#  Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в новый файл

# еще не сделал... в процессе...
# book = []
# b = {}
# n = 0
# seq = 0
# in_file = open("E:\\work\\python_script\\work\\dep.txt", 'r')
# read = in_file.readline()
# table_count = len(read.split())   # определяем сколько столбцов в таблице
# str_count = len(in_file.readlines())
# print(table_count,str_count)
# in_file = open("E:\\work\\python_script\\work\\dep.txt", 'r')
# #for massiv in read:
# read = in_file.readline()
# reads = read.join(read.split())
# reads = read.split()
# for ss in range(table_count):
#     read2 = in_file.readline()
#     reads2 = read2.split()
#     #reads2 = reads2+ ss
#     for ss2 in range(str_count):
#         print(ss,  reads[ss], reads2)
#     b.update({reads[ss] : reads[ss]})
# print(b)
