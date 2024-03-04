import sys
import math as m
import random as r
from collections import defaultdict

def zad1():
        napis = input("Podaj napis: ")
        tmp = len(napis.split())
        print(tmp)
# zad1()


def zad2():
    sys.stdout.write("Podaj liczbę a: ")
    a = int(sys.stdin.readline())
    sys.stdout.write("Podaj liczbę b: ")
    b = int(sys.stdin.readline())
    sys.stdout.write("Podaj liczbę c: ")
    c = int(sys.stdin.readline())
    print(m.pow(a,b)+c)
# zad2()


def zad3():
    napis = input("Podaj napis: ")
    return napis == napis[::-1]
# print(zad3())


def zad4():
    x = int(input("Podaj liczbę: "))
    tmp = 0
    for i in range(1,x+1):
        if x % i == 0:
            tmp = tmp + 1
    if tmp == 2:
        return True
    return False


# print(zad4())

def zad5():
    suma = 0
    tmp = []
    wynik = []
    for i in range(3,1001):
        for j in range(2,i+1):
            if i % j == 0:
                tmp.append(j)
        for k in range(0, len(tmp)):
            suma = suma + tmp[k]
        if suma == i:
            wynik.append(i)
        tmp.clear()
    print(wynik)


zad5()

def zad6():
    x = [r.randint(1, 100), r.uniform(1.0, 100.0), r.randint(1, 100), r.uniform(5.0, 50.0)]
    print(x)
    for i in range(0, len(x)):
        x[i] = m.pow(x[i], 2)
    print(x)


# zad6()


def zad7():
    tmp = []
    i = 1
    while i <= 10:
        x = float(input("Podaj liczbę: "))
        if x % 2 == 0:
            tmp.append(x)
        i = i+1
    print(tmp)


# zad7()


def zad8():
    x = [r.randint(1, 100), 42,  r.uniform(1.0, 100.0), 42,"asd", r.randint(1, 100), r.uniform(5.0, 50.0), "asd"]
    slownik = defaultdict(int)
    for i in x:
        slownik[i] += 1
    print(slownik)

    for j in list(slownik.keys()):
        if not isinstance(j,(int, float)):
            del slownik[j]
    print(slownik)
# zad8()