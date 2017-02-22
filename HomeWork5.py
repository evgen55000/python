# Задания 1
# Записываем “Number: строка из файла” (где Number – порядковый номер
# строки) из одного файла в другой, открытый для записи двумя способами:
#  Циклом
#  Методами readlines и writelines

a = 0
file = open("E:\\work\\python_script\\python\\test.txt",'r')
for line in file:
    a = a + 1
    print('number:', a, line.rstrip())
    print('number:',a, line.rstrip(), file=open('E:\\work\\python_script\\python\\test2.txt','a+'))
file.close()

a = 0
file_open = open("E:\\work\\python_script\\python\\test.txt",'r')
file_write = open('E:\\work\\python_script\\python\\test3.txt','w+')
read = file_open.readlines()
for line in read:
    a = a + 1
#    print('number:',a, line.rstrip())
    print('number:',a,  line.rstrip(), file=file_write)
file_open.close()
file_write.close()

# не рабочая версия
# a = 0
# file_open = open("E:\\work\\python_script\\python\\test.txt",'r')
# file_write = open('E:\\work\\python_script\\python\\test4.txt','w+')
# #read = file_open.readline()
# for line in file_open.readline():
#     a = a + 1
#     print('number:',a, line.rstrip())
#    # print('number:',a,  line.rstrip(), file=file_write)
# file_open.close()
# file_write.close()

# Задание 2
# Имеем список слов. Если слова начинаются на первые три буквы алфавита,
# вывести эти слова на экран и записать эти слова в файл.
# А теперь используя выражение continue?

import re
data = []
in_file = open("E:\\work\\python_script\\python\\test.txt",'r')
read = in_file.readlines()
for data in read:
    if re.findall(r'ABC',data):
        print(data.rstrip())
        print(data.rstrip(), file=open('E:\\work\\python_script\\python\\test7.txt', 'a+'))
in_file.close()


# Задание 3
# В вечном цикле у пользователя приглашение на ввод. Если пользователь вводит
# больше чем одно слово, программа игнорирует этот ввод (используйте
# выражение continue). Если вводит одно слово, программа «говорит» спасибо +
# запоминает эти слова в список, и, если пользователь второй раз введет такое же
# слово, она объявит, что уже знает это слово).

import re
while True:
    a = input('Введите одно слово ')
    if  re.findall(r' ',a):
        continue
    in_file = open("E:\\work\\python_script\\python\\test9.txt", 'r')
    read_in = in_file.readlines()
    for read in read_in:
        #print(read)
        if re.findall(a,read):
            print('Я уже знаю это слово')
            break
    else:
        print('Спасибо ')
        print(a.rstrip() , file=open('E:\\work\\python_script\\python\\test9.txt', 'a+'))
        in_file.close()

# Задание 4
# Удалите все элементы со значением 'ABC' из списка (Используя remove метод и цикл)


# Задание 5
# Сгенерируйте список длин элементов-строк из списка, если в элементе
# действительно строки (это вы проверите в if части)
# используя [expression for item in iterable if condition]




# Задание 5* (доп.)
# Сгенерируйте список слов (переведя все слова в нижний регистр, т.е. все
# маленькими буквами) из файла. Проверьте, что то, что вы добавляете, это слово
# (методом isalpha)
# А теперь попробуйте, используя l = [expression for item in iterable if condition]