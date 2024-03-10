import sys

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
for i in range(1, 1000):
    suma_dzielinikow_i = 0
    for j in range(1, i):
        if i % j == 0:
            suma_dzielinikow_i += j
    if suma_dzielinikow_i == i:
        ile_doskonalych += 1
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
# zadanie 3.8
lista = ['a', 'a', 'a', 'b', 'b', 1, 1, 1, 2, 2, 2, 3, 3, 3, 'c', 'c', 5, 5, 5]
slownik = {}
for i in range(0, len(lista)):
    if lista[i] not in slownik:
        ile_razy = 0
        for j in range(0, len(lista)):
            if lista[i] == lista[j]:
                ile_razy += 1
        slownik.update({lista[i]: ile_razy})
list_of_keys = list(slownik.keys())
print(type(list_of_keys))
for i in range(0, len(list_of_keys)):
    try:
        a = float(list_of_keys[i])
    except ValueError:
        slownik.pop(list_of_keys[i])
print(slownik)
