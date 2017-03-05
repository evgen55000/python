# Задание 5
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и
# возвращающую True, если год високосный, и False иначе.
# (Напомним, что в соответствии с григорианским календарем, год является високосным, если
# его номер кратен 4, но не кратен 100, а также если он кратен 400.)

def is_year_leap(a):
    if ((a/4 == a//4) and (a//100 != a/100)) or (a//400 == a/400): return True #не високосный
    else: return  False #високосный
#print(is_year_leap(2200))

# Задание 6
# Написать функцию is_date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.
# Используйте в этой функции функцию is_year_leap для определения сколько дней в феврале.

import datetime
def is_date(year,month,day):
    g = is_year_leap(year)
    m = 0
    s = False
    if year > 1:
        if 1 <= month <= 12:
            if month == 2:
                if g == True:
                    m = 29
                else: m = 28
            else:
                if month/2 == month//2:
                    m = 31
                else:
                    m = 30
            if 1 <= day <= m:
                #print('good')
                s = True
                assert datetime.date(year, month, day)
            else:
                s = False
 #       else:
    return s

print(is_date(2020,11,30))