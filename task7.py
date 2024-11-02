# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
n = int(input())
m = int(input())
k = int(input())
def is_valid_triangle(n, m, k):
    if n < m+k or m < n+k or k < n+m:
        return True
    else:
        return False

print(is_valid_triangle(n,m,k))

