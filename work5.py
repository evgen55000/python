# files = 'test5.txt'
# files_full = 'E:\\work\\python_script\\python\\'+ files
# input_file = open(files_full,'a+')

#
# input_file = open("E:\\work\\python_script\\python\\test.txt")
# #read = input_file.readline()
# for line in input_file:
#     print('number' line.rstrip() + '!')
#
# print(type(input_file))

# a = 'world'
# for m in a:
#     print(m*3,end='')
# a = ['s','r',1,4,5]
# print(a)
# a[2] = '77'
# print(a)
# a[-1] = 'hell'
# print(a)
# a = a * 4
# print(a)
# b = [3,5,6]
# a = a+b
# print(a)

# a = ['s','r',1,4,5]
# a.append([1,4,6])
# print(a)
# a[a.index([1,4,6])].append(77)
# print(a)
# b = a.index([1,4,6,77])
# print(c)

res = [i**2 for i in range(1,26,2)]
print(res)
b = [3,4,6,7]
res = [i**2 for i in b]
print(res)

b = ['gdf','gdf','hg','yu']
res = [b[0] for b in  b ]
print(res)