from math import *
#
# # exceptions
# # python comprehension
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l1 = []
# for i in list1:
#     l1.append(i ** 2)
# print(l1)
# l2 = [x ** 2 for x in list1]
# print(l2)
# l3 = [pow(3, y) for y in range(0, 6)]
# print(l3)
# l4 = [x for x in l2 if x % 2 == 1]
# print(l4)
#
# s1 = {1: 2, 3: 4, 5: 6, 7: 8}
# s2 = {}
# for key, value in s1.items():
#     s2[value] = key
# print(s1)
# print(s2)
# s3 = {v: k for k, v in s1.items()}
# print(s3)
#
#
# def rownanie_kwadratowe(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print("brak pierwiastkow")
#         return 0
#     elif delta == 0:
#         x = (-b) / (2 * a)
#         print("jeden peirwiastek")
#         return x
#     elif delta > 0:
#         print("dwa pierwiastki")
#         x1 = (-b + sqrt(delta)) / (2 * a)
#         x2 = (-b - sqrt(delta)) / (2 * a)
#         return x1, x2
#
#
# print(rownanie_kwadratowe(6, 1, 3))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(1, 4, 2))
#
#
# def dlugoscodcinka(x1=0, y1=0, x2=0, y2=0):
#     return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#
# print(dlugoscodcinka())
# print(dlugoscodcinka(3, 0, 1, 1))


plik = open('plik.txt')
print(plik)
