# Задания 1
# Попросите пользователя ввести слово без пробелов. Пока он не введёт
# правильно, просите его ввести. Проверьте, что вы правильно закодили с помощью assert инструкции

import re
while True:
    a = input('введите слово без пробелов: ')
    if re.findall(r' ', a):
        print('есть пробелы')
        assert re.findall(r' ', a)
    else:
        print('Спасибо')
        break


# Задание 2
# Делаем из задания функцию «Считываем текст из файла. Посчитываем сколько в
# нем используется слов (уникальных).» Передавайте как аргумент разные файлы. Протестируйте функцию.

def addfile(namefile='1',c_unic=0):
    assert namefile != '1'
    assert namefile != 'test.txt'
    assert c_unic != 0
    op_file = "E:\\work\\python_script\\work\\" + namefile
    print(op_file,c_unic)
    out_file = open(op_file, 'w+')
    print(c_unic, file=out_file)
    out_file.close()
    return

unic = set()
in_file = open("E:\\work\\python_script\\work\\test.txt", 'r')
read = in_file.read()
read = read.split()
for i in read:
    i = i.rstrip()
    unic.add(i)
b = len(unic)
print(b)
addfile('t1.txt',b)
addfile('t2.txt',b)
addfile('',b) #проверяем как работает assert

# Задание 3
# Пишем функцию, которая выводим второе по возрастанию значение из
# переданных аргументов. Учитываем, что может быть повторяющиеся значения аргументов.

# еще не сделал....
# def func(*read):
#     a1 = []
#     #assert type(read) != str
#     print(read)
#     unic = set()
#     for i in read:
#         unic.add(i)
#         print(i)
#     a = i
#     a1 = sorted(a)
#     print('fsdfds',a1)
#     return a1[1]
#
# print(func(1,7,66,5,3,55,4,1))


# Задание 4
# Пишем функцию, которая генерирует песню la-la- la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце стоит точка, если 1, то в конце стоит «!»