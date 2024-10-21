# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
n = int(input())
m = int(input())

def grobdaly(n, m):

    if n == m:
        return n

    while n != m:
        if n > m:
            n-=m
        if n < m:
            m -= n
    return n
print(grobdaly(n, m))