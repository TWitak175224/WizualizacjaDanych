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
