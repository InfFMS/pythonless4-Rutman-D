# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!
n = int(input())

def N(n):
    if n == 2:
        return "YES"
    elif n < 2:
        return "NO"
    return N(n/2)

print(N(n))

n = int(input())

def N(n):
    if n == 2 or n == 1:
        return "YES"
    elif n < 2:
        return "NO"
    return N(n/2)

print(N(n))