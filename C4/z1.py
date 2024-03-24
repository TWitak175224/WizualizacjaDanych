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

macierz = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])
print(macierz)
liczby = np.arange(1, 2, 0.1)
print(liczby)

linczby_lin = np.linspace(1, 2, 5, )
print(linczby_lin)

z = np.indices((5, 3))
print(z)
print()

print(z[0, 3, 1])
print()
x, y = np.mgrid[0:5, 0:5]
print(x)
print()
print(y)
print()

mat_diag_k = np.diag([a for a in range(5)])
print(mat_diag_k)
print()
mat_diag_k = np.diag([a for a in range(5)], k=-1)
print(mat_diag_k)
print()
mat_diag_k = np.diag([a for a in range(5)], k=1)
print(mat_diag_k)
print()

z = np.fromiter(range(5), dtype='int32')
print(z)

znaki = b'abcdef'  # przekaanie znaków jako ciąg bajtów
zn1 = np.frombuffer(znaki, dtype='S1')
print(zn1)
zn2 = np.frombuffer(znaki, dtype='S2')
print(zn2)

znaki = "abcdef"
zn3 = np.array(list(znaki))
zn4 = np.array(list(znaki), dtype='S1')
zn5 = np.array(list(b'abcdef'))
zn6 = np.fromiter(znaki, dtype='S1')
zn7 = np.fromiter(znaki, dtype='U1')
print(zn3)
print(zn4)
print(zn5)
print(zn6)
print(zn7)

mat = np.ones((2, 2))
mat_1 = np.ones((2, 2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat * mat_1)
print(mat / mat_1)
print(mat / [[3, 5], [6, 1]])

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
print(a[2:7:2])
print(a[1:])
print(a[2:5])
