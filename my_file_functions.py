def fs(namefile, *book ):
    a = b = c =  0
    file_dir = "E:\\work\\python_script\\work\\" + namefile
    in_file = open(file_dir, 'r')
    in_file = (in_file.read()).split()
    for book2 in book:
        book2 = book2.rstrip()
        #print(book2)
        if len(book2) == 1: # определяем это слово или нет?
            #print('one')
            if ('a'<=book2<='z') or ('A'<=book2<='Z'): #определяем это буква?
                for i in in_file:
                    if i[:1] == book2: #ищем сколько первых букв
                        a += 1
                    if i.find(book2) != -1: # в скольких словах
                        b += 1
                print('начинающиеся на этот символ- ' ,a,'в скольких словах встречается эта буква- ',b )
            else:
                for i in in_file:
                    c = i.count(book2) + c
                print('символ, результат: сколько раз встречается этот символ- ',c)
        else:
            print('сколько раз встречается это слово: ', in_file.count(book2) )

    return #namefile