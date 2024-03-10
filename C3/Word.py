import random
import math
A = [1 - x for x in range(1, 11)]
print(A)
B = [4 ** x for x in range(8)]
print(B)
C = [x for x in B if not (x % 2)]
print(C)

# zad2
lista1 = [random.randint(0, 2000) for x in range(10)]
lista2 = [x for x in lista1 if not (x % 2)]
print(lista1)
print(lista2)
# zad 3
slownik = {"ziemniaki": "kg", "jogurt": "opakowania", "mleko": "kartony", "wedlina": "plastry", "ananas": "sztuki"}
slownik_sztuk = {key: value for key, value in slownik.items() if slownik[key] == "sztuki"}
print(slownik_sztuk)


# zad 4

def czy_trojkat_prostokatny(a, b, c):
    return (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2)


print(czy_trojkat_prostokatny(3, 4, 5))
print(czy_trojkat_prostokatny(1, 2, 3))


# zad 5
def pole_trapezu(a=2, b=1, h=1):
    return ((a + b) / 2) * h


print(pole_trapezu(10, 11))


# zad 6
def iloczyn_ciagu(a=1, b=4, ile=10):
    iloczyn = 1
    for i in range(ile):
        iloczyn *= a * (b ** i)
    return iloczyn


print(iloczyn_ciagu(1, 2, 3))

#zad 7
a=float(input("podaj liczbe do pierwiastkowania"))
try:
    a = math.sqrt(a)
    print(a)
except ValueError:
    print("Liczba ujemna! Nie oblicze pierwiastka!")


