# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3

n = int(input())
m = int(input())

def nod(n, m):
    if n == m:
        return n
    while n != m:
        if n > m:
            n -= m
        if n < m:
            m -= n
    return n

def drob(m, n):
    i = nod(m, n)
    m = m / i
    n = n / i
    print(m, n)
drob(n, m)


