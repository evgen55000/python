# in_file = open("E:\\work\\python_script\\work\\spisok.txt")
# sp = []
# b = 0
# a = 0
# for read in in_file:
#     sp = read.split()
#     a+=1
#     print(sp, len(read))
#     if len(read)-1 >=2 or (sp[0:] == sp[:-1]):
#         b +=1
# print(a,b)
# in_file.close()

# a = [3,5,3,6,6,7,8]
# b = []
# for sp in range(0,len(a)-1):
#     print (a[sp])
#     if a[sp] == a[sp+1]:
#         b.append(a[sp])
#
#         print(b)


# d = {}
# d = {'dict':1,'dictionary':2}
#d = {5: 'dict',10.4: 'dictionary','five':5,(1,1):5}
# d = dict(short='dict',long='ok')
# d = dict([(1,1),(2,4)])
# d = {1:2,3:4,4:9}
# d[5] = 4**2

#
# for a in d:
#     print(a, ':', d[a])
#
# for key,value in d.items():
#     print(key,value)
#

# a = ['hell','day','you','number']
# set(a)
# m = 'day' in a
# print(m)



a = ['1','hell','3','you4',5,5,5,6,7]
a = set(a)
print(len(a))
