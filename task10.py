# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.
n = int(input())
f = int(input())
t = int(input())


def convert_base(n,f,t):
    tmp = n%10
    tmp1 = 0
    tmp2 = ""
    for i in range(len(str(n))):
        tmp1 += tmp*(f**i)
        tmp = n%(10**(i+2))//(10**(i+1))

    for i in range(len(str(tmp1)), 1, -1):
        print("I", tmp1, tmp2, i)
        tmp2 += str(tmp1%t)
        tmp1 = tmp1%t
        print("II", tmp1, tmp2, i)
    return tmp2

print(convert_base(n,f,t))

#НЕ ДОПИСАЛ

