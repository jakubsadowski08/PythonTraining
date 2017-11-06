import math, time


def pobierz_zapelniona_liste(maximum):
    return [True]*(maximum + 1)


def zmiana_wartosci(lista, maximum):
    i = 2
    while i < math.sqrt(maximum + 1):
        if lista[i]:
            for j in range(i * i, maximum + 1, i):
                lista[j] = False
        i = i + 1


def przepisanie_liczb_pierwszych(lista, maximum, liczby_pierwsze):
    for i in range(2, maximum + 1):
        if lista[i]:
            liczby_pierwsze.append(i)


def main(maximum):
    Sito_Eratostenesa = pobierz_zapelniona_liste(maximum)
    liczby_pierwsze = []
    zmiana_wartosci(Sito_Eratostenesa, maximum)
    przepisanie_liczb_pierwszych(Sito_Eratostenesa, maximum, liczby_pierwsze)
    return liczby_pierwsze


start_time = time.time()
liczby_pierwsze = main(10000000)
print(liczby_pierwsze[-10:-1])
print("--- %s seconds ---" % (time.time() - start_time))
