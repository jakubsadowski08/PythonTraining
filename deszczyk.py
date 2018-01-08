import random
tablica = []
for i in range(10):
    x = random.randint(1, 10)
    ciag = "0" * (x - 1) + "x" + "0" * (10 - x)
    tablica.insert(0,ciag)
    for j in range(len(tablica)):
        print(tablica[j])
    for j in range(10 - len(tablica)):
        print("0" *10)
    print()
    print()
