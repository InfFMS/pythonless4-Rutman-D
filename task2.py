# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
n = int(input())

def number_to_words(n):
    a = ["один","два","три","четыре","пять","шесть","семь","восемь","девять"]
    b = ["десять","одинадцать","двенадцать","тренадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
    c = ["двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"]
    if n >= 20:
        print(c[n//10-2], a[n%10-1])
    elif n >= 10 and n < 20:
        print(b[n%10])
    else:
        print(a[n-1])

number_to_words(n)



#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять