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

