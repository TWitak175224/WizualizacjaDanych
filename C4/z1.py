import numpy as np

a = np.array([0, 1])
print(a)

a = np.arange(2)
print(a)
print(type(a))

print(a.dtype)
a = np.arange(2, dtype='int32')
print(a)
print(a.dtype)
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)

print(a.ndim)

m = np.array((np.arange(2), np.arange(2)))
print(m)
print(m.shape)
print(m.ndim)

m2 = np.array([[1, 2, 3], [3, 23, 34], [2.3, 2.3, 3.2]])

print(m2)
print(m2.shape)

wektor = np.arange(5)
print(wektor)

zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2, 2))
print(pusta)
poz1 = pusta[1, 1]
poz2 = pusta[0, 1]
print(poz1)
print(poz2)

macierz = np.array([[1,2],[3,4],[5,6]])
print(macierz)
liczby = np.arange(1,2,0.1)
print(liczby)

linczby_lin = np.linspace(1,2,5)
print(linczby_lin)
