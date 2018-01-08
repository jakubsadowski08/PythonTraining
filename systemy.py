from random import randint
import time
import os

def char_na_liczbe(char):
    if char.isdigit():
        return int(char)
    else:
        return ord(char) - 55
system_1 = int(input("Podaj system: "))
liczba = input("Napisz cos w tym systemie: ")
dlugosc = len(liczba) - 1
wynik = 0
for i in liczba.upper():
    wynik = wynik + char_na_liczbe(i) * system_1**dlugosc
    dlugosc = dlugosc - 1
print(wynik)

