# s,i = 's',0
# try:
#     s =int(s) / i
#     except valuerror as e:
#         print('e')
#     except zerodivisionerror:
#         print('zero')

#
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print('unknown_var')
# finally:
#     print('privet')

#
# a = 0
# in_file = open("E:\\work\\python_script\\work\\dep.txt", 'r')
# read = in_file.read()
# reads = read.split()
# try:
#     for rr in reads:
#         try:
#             print(rr)
#             a = int(rr)
#         except:
#             print("err")
#         finally:
#             print('final for')
# except:
#     print('err',a)
# else:
#     print('Idid it!',a)
# finally:
#     print('ff',a)

# a = 'errrr'
# name = '3Lena'
# if name[0].isnumeric():
#     raise NameError(a)
# print('ok',a)

# while True:
#     a = input('ведите число ')
#     try:
#         a = int(a)
#     except:
#         print('ne to')
#     else:
#         print('OK',a)
#         break
#     finally:
#         print(a,' это не число')
#

# a = [1,2,3,4,5]
# a = []
# def adds(a):
#     try:
#         a[0],a[-1] = a[-1],a[0]
#     except:
#         return 'ne ok'
#     else:
#         return a
# print(adds(a))
# #print(a)

# def func(a,b,c=2):
#     return a+b+c
# func(a=3,c =6,b=7)


def func(*r):
    print(r)
    a = sorted(r)
    return a[1]
print(func(7,66,5,3,55,4,1))
