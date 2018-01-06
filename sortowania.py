#Jakub Sadowski
import random
import math
import copy

def losuj():
    tab = []
    for i in range(11000):
        tab.append(random.randint(1, 50))
    return tab


def sortowanie_babelkowe(tab):
    for i in range(len(tab) - 1, 0, -1):
        for j in range(i):
            if tab[j + 1] < tab[j]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]


def sortowanie_wybieranie(tab):
    for i in range(0, len(tab) - 1):
        min_index = i
        for j in range(i, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]


def sortowanie_wstawianie(tab):
    for i in range(1, len(tab)):
        klucz = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > klucz:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = klucz


def podziel(tab, l, r):
    pivot = l
    for i in range(l + 1, r + 1):
        if tab[i] <= tab[l]:
            pivot += 1
            tab[i], tab[pivot] = tab[pivot], tab[i]
    tab[pivot], tab[l] = tab[l], tab[pivot]
    return pivot


def sortowanie_szybkie(tab, l=0, r=None):
    if r is None:
        r = len(tab) - 1
    if l < r:
        pivot = podziel(tab, l, r)
        sortowanie_szybkie(tab, l, pivot - 1)
        sortowanie_szybkie(tab, pivot + 1, r)
    return tab


def scalanie(tab, l, srodek, r):
    i = l
    j = srodek + 1
    tab2 = []
    while i <= srodek and j <= r:
        if tab[j] < tab[i]:
            tab2.append(tab[j])
            j = j + 1
        else:
            tab2.append(tab[i])
            i = i + 1
    if i <= srodek:
        while i <= srodek:
            tab2.append(tab[i])
            i = i + 1
    else:
        while j <= r:
            tab2.append(tab[j])
            j = j + 1
    s = r - l + 1
    i = 0
    while i < s:
        tab[l + i] = tab2[i]
        i = i + 1

    return tab


def sortowanie_scalanie(tab, l=0, r=None):
    if r is None:
        r = len(tab) - 1
    if l != r:
        srodek = int(math.floor((l + r) / 2))
        sortowanie_scalanie(tab, l, srodek)
        sortowanie_scalanie(tab, srodek + 1, r)
        scalanie(tab, l, srodek, r)
    return tab


def kopiec(tab, n, i):
    maximum = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and tab[i] < tab[l]:
        maximum = l
    if r < n and tab[maximum] < tab[r]:
        maximum = r
    if maximum != i:
        (tab[i], tab[maximum]) = (tab[maximum], tab[i])
        kopiec(tab, n, maximum)


def sortowanie_kopcowanie(tab):
    n = len(tab)
    for i in range(n, -1, -1):
        kopiec(tab, n, i)
    for i in range(n - 1, 0, -1):
        (tab[i], tab[0]) = (tab[0], tab[i])
        kopiec(tab, i, 0)

tab = losuj() #dane wejsciowe

test = copy.copy(tab)#za kazdym razem te same dane
print(tab)

sortowanie_wybieranie(test)
print(test)

test = copy.copy(tab)
sortowanie_wstawianie(test)
print(test)

test = copy.copy(tab)
sortowanie_babelkowe(test)
print(test)

test = copy.copy(tab)
sortowanie_szybkie(test)
print(test)

test = copy.copy(tab)
sortowanie_scalanie(test)
print(test)

test = copy.copy(tab)
sortowanie_kopcowanie(test)
print(test)
