# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7



def primes(n, i=2):
    if n <= 1:
        return
    if n % i == 0:
        print(i)
        primes(n//i, i)
    else:
        primes(n, i+1)


n = int(input())

primes(n)

