# import triangle
# x = int(input())
# y = int(input())
# print(triangle.sq(x,y))


# def func(**kwargs):
#     return kwargs.get('name') + ' is ' + kwargs.get('job') + str(kwargs.get('mails'))
# print(func(name='ok', job='commit', mails=2))

# l = ["jon","lili","ann"]
# print(*l)
# print(l)

# import math
# print(dir(math))
# import builting
# print(dir(builting))

# x = 0
# def ss():
#     print('privet',x)
#     x = x +  1
#     ss()
# ss()


# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(1,10):
#     print(fib(i))

#
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(2))

# print((lambda x,y: x**3/y)(4,5))

#print((lambda x: x**3)('5'))
func = (lambda x: len(x) < 10)

print(func('fsdfdsf'))
print((lambda x: len(x) < 10)('fdnhsdkjfhskl'))