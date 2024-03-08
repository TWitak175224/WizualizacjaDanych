import sys
import math

# a = 56
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# zmienna_tekstowa = "Wizualizacja danych"
# print(zmienna_tekstowa)
# print(type(zmienna_tekstowa))
#
# c = a // b
# print("dzieleie całkowite(//), czyli obcina część po przecinku")
# print("potęgowanie roi się ** użyteczny gdy nie ułamki, albo pow() cały czas")
# # 6**1/2 zwraca 3 bo robi w kolejości (6**1)/2 więc trzeba uzywać nawiasów 6**(1/2) da pierwiastek z 6
# print('liczba a jest rowna {:d}, a liczba b jest rowna {:.2f}'.format(a, b))
# a = input('Wpisz liczbe: ')
# print(a + " wartosc ")
# a = int(a)
# print(a)
# sys.stdout.write('Wprowadz cyfre: ')
# b = sys.stdin.readline()
# print(b + "wartosc")
# print(type(b))
# b = int(b)
# print(type(b))
#
# lista = [5, 6.6, "asa", 56, 84, "isi", [1, 2, 3]]
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(1, 'c')
# print(lista)
# lista.extend("abba")
# print(lista)
# lista.pop()
# print(lista)
# lista.remove([1, 2, 3])
# print(lista)
# del lista[1]
# print(lista)
# #del lista usunie całą listę!
# print(lista)
# lista.reverse()
# # lista.sort()
# # do sorta wchodzi lista możliwa do posortowania
#
# slownik = {'klucz': 'wartosc', 1: 2, 'a': 3, 'b': 'a'} # wartosci kluczy unikatowe, inaczej nastapi nadpisanie
# print(slownik['a'])
# slownik[6] = 45
# print(slownik)
# print(slownik[6])
# slownik.pop(6)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
#
# a = 6
# b = 7
# if a > b:
#     print("a is greater than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("b is greater than a")
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if (a > b) | (c > d):
#     print(a, c)
# else:
#     print(b, d)
#
# for i in range(8):
#     print(i)
#
#
# lista = [5, 6.6, "asa", 56, 84, "isi", [1, 2, 3]]
# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print("koniec petli")
#

# lista = [2, 3, 5, 7, 12312, 12345, 6789, 543]
# a = int(input())
# licznik = 0
# while licznik < len(lista):
#     if (a - lista[licznik])!=0:
#         break
#     licznik+= 1
# else:
#     print('żadna z listy nie zeruje Twojej liczby')

#### TUTAJ zaczynają się zadania

# zadanie 1.1
a, b = 1, 2
c, d = 'aaaa', 'bbbb'
e, f = 3.14, 5.21
print(type(a), type(b), type(c), type(d), type(e), type(f))

# zadanie 1.2
a, b = float(input('Enter first number: ')), float(input('Enter second number: '))
c = int(input("wybierz działanie:\n1 - dodawanie,\n2- odejmowanie\n3 - mnożenie\n4 dzielenie\n"))
if c == 1:
    print(a + b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a * b)
elif c == 4:
    print(a / b)

# zadanie 1.3
a = 5
a **= 2
print(a)
a = 5
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)

# zadanie 1.4
pierwsza = math.exp(10)
print(pierwsza)
druga = pow(math.log((5 + pow(math.sin(8), 2)), math.exp(1)), 6)
print(druga)
trzecia = math.floor(3.55)
print(trzecia)
czwarta = math.ceil(4.80)
print(czwarta)

# zadanie 1.5
del a, b, c, d, e, f, pierwsza, druga, trzecia, czwarta
imie = 'TOMASZ'
nazwisko = 'WITAK'

print(imie.capitalize())
print(nazwisko.capitalize())

# zadanie 1.6

piosenka = 'la la la hahah ahah'
a = piosenka.count('la')
print(a)

# zadanie 1.7

napis = 'przenosze góry i doliny'

print(napis[1] + napis[len(napis) - 1])

# zadanie 1.8
print(piosenka.split(' '))

# zadanie 1.9
a = 'pioseneczka'
b = 15.3
c = 0xabc16

print('string ' + a + ' float ' + str(b) + " hex " + str(c))

# zadanie 2.1

lista = ['szachy', 'siatkowka', 'lekkoatletyka']
lista.reverse()
lista.append('boks')
print(lista)

# zadanie 2.2
del lista, a, b, c, piosenka, napis, imie, nazwisko

slownik = {'m.in': 'między innnymi', 'pok': 'pokazane', 'np': 'na przykład'}

# zadanie 2.3
del slownik
slownik = {'Fallout': 'RPG', 'EUIV': 'Strategia', 'Grounded': 'survival', 'Skyrim': 'RPG'}
print(slownik)

# zadanie 2.4
a = input()
print(a.count('a'))

# zadanie 2.5
sys.stdout.write('podaj a')
a = int(sys.stdin.buffer.readline())
sys.stdout.write('podaj b')
b = int(sys.stdin.buffer.readline())
sys.stdout.write('podaj c')
c = int(sys.stdin.buffer.readline())
sys.stdout.write(str(pow(a, b) + c))

# zadanie 2.6
a, b, c = float(input('podaj a ')), float(input('podaj b ')), float(input('podaj c '))
if a > b:
    if a < c:
        print(c)

    else:
        print(a)
elif c > b:
    print(c)
else:
    print(b)

# zadanie 2.7
lista_int, lista_float = [1, 2, 3, 4, 5], [1.2, 2.3, 3.4, 4.5, 5.6]
for i in range(0, len(lista_int)):
    lista_int[i] = pow(lista_int[i], 2)
for i in range(0, len(lista_float)):
    lista_float[i] = pow(lista_float[i], 2)

# zadanie 2.8
tablica, i = [], 0
while i < 10:
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        tablica.append(a)

print(tablica)
del tablica, lista_int, lista_float, a, b, c

# zadanie 2.9
a = int(input("Podaj liczbe: "))
if a < 0:
    print("pierwiastkowana liczba musi być większa od 0")
else:
    print(pow(a, (1 / 2)))  # zrobione na około, ponieważ python nie wyrzucał błędu

# zadanie 3.1
zdanie = input("Podaj zdanie :")
slowa = zdanie.split(' ')
ile_slow = 0
for i in range(0, len(slowa)):
    if slowa[(len(slowa) - 1 - i)]:
        ile_slow += 1
print(ile_slow)

# zadanie 3.2
sys.stdout.write('podaj a')
a = int(sys.stdin.buffer.readline())
sys.stdout.write('podaj b')
b = int(sys.stdin.buffer.readline())
sys.stdout.write('podaj c')
c = int(sys.stdin.buffer.readline())
sys.stdout.write(str(pow(a, b) + c))
# zadanie 3.3
napis = input()
flag = 0
for i in range(len(napis)):
    if napis[i] != napis[len(napis) - i - 1]:
        flag = 1
        break
if flag:
    print('nie palindrom')
else:
    print('palindrom')

# zadanie 3.4
a = int(input())
flag = 0
for i in range(2, pow(a, 1 / 2)):
    if a % 1 == 0:
        flag = 1
        break

if flag == 1:
    print('nie jest liczba pierwszą')
else:
    print('jest liczba pierwsza')

# zadanie 3.5
ile_doskonalych = 0
for i in range(1,1000):
    suma_dzielinikow_i = 0
    for j in range(1,i):
        if i%j==0:
            suma_dzielinikow_i +=j
    if suma_dzielinikow_i==i:
        ile_doskonalych+=1
print(ile_doskonalych)
# zadanie 3.6
lista_int, lista_float = [1, 2, 3, 4, 5], [1.2, 2.3, 3.4, 4.5, 5.6]
for i in range(0, len(lista_int)):
    lista_int[i] = pow(lista_int[i], 2)
for i in range(0, len(lista_float)):
    lista_float[i] = pow(lista_float[i], 2)

# zadanie 3.7
tablica, i = [], 0
while i < 10:
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        tablica.append(a)

print(tablica)
#zadanie 3.8
lista =['a','a','a','b','b',1,1,1,2,2,2,3,3,3,'c','c',5,5,5]
slownik = {}
for i in range(0,len(lista)):
    if lista[i] not in slownik:
        ile_razy=0
        for j in range(0,len(lista)):
            if lista[i]==lista[j]:
                ile_razy+=1
        slownik.update({lista[i]:ile_razy})
list_of_keys=list(slownik.keys())
print(type(list_of_keys))
for i in range(0,len(list_of_keys)):
    try:
        a = float(list_of_keys[i])
    except ValueError:
        slownik.pop(list_of_keys[i])
print(slownik)