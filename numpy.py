import numpy as np

def zad1():
    tablica = np.arange(3, 46, 3)
    print(tablica)
# zad1()

def zad2():
    lista_float = [1.5, 2.7, 3.9, 4.2, 5.1]
    lista_int64 = np.array(lista_float, dtype=np.int64)
    print(lista_float)
    print(lista_int64)
# zad2()

def zad3(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("'n' musi być dodatnią liczbą całkowitą.")
    tablica = np.arange(1, n * n + 1).reshape(n, n)
    return tablica
# print(zad3(4))

def zad4(podstawa, ilosc):
    if ilosc <= 0:
        raise ValueError("Ilość musi być liczbą dodatnią.")
    tablica_poteg = np.logspace(0, ilosc - 1, num=ilosc, base=podstawa, dtype=int)
    return tablica_poteg
# print(zad4(2,4))

def zad5(dlugosc):
    if not isinstance(dlugosc, int) or dlugosc <= 0:
        raise ValueError("Długość wektora musi być dodatnią liczbą całkowitą.")
    wektor_odw = np.arange(dlugosc, 0, -1)
    mdiag = np.diag(wektor_odw)
    return mdiag
# print(zad5(5))

def zad6(s1, s2, s3):
    dlugosc = max(len(s1), len(s2), len(s3))
    macierz = np.empty((dlugosc, dlugosc), dtype='U1')
    macierz[:len(s1), :len(s1)] = np.array(list(s1)).reshape(len(s1), 1)
    macierz[:len(s2), -1] = np.array(list(s2))
    macierz[-1, :len(s3)] = np.array(list(s3))
    return macierz
# print(zad6("abc","qwe","xyz"))

def zad7(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("'n' musi być dodatnią liczbą całkowitą.")
    macierz = np.zeros((n, n), dtype=int)
    for i in range(n):
        macierz[i, i] = 2
        if i > 0:
            macierz[i, i - 1] = 4
        if i < n - 1:
            macierz[i, i + 1] = 4

    return macierz
# print(zad7(3))

def zad8(tablica,kierunek):
    if kierunek == 'pionowo':
        if tablica.shape[0] % 2 != 0:
            print("Liczba wierszy jest nieparzysta.")
            return None
        else:
            polowa = tablica.shape[0] // 2
            return tablica[:polowa], tablica[polowa:]
    elif kierunek == 'poziomo':
        if tablica.shape[1] % 2 != 0:
            print("Liczba kolumn jest nieparzysta.")
            return None
        else:
            polowa = tablica.shape[1] // 2
            return tablica[:, :polowa], tablica[:, polowa:]

tablica = np.array([[1, 2], [4, 5]])
# print(zad8(tablica,"pionowo"))

def zad9(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
macierz_fibonacci = np.array(zad9(25)).reshape(5, 5)
print(macierz_fibonacci)