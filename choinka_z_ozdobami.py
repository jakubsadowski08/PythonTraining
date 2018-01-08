n = int(input("PODAJ WYSOKOSC : "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    if i % 2 == 0:
        for j in range(2 * i - 1):
            if (j + 3) % 4 == 0:
                print("o",end='')
            else:
                print("x",end='')
    else:
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("!",end='')
            else:
                print("x",end='')
    print()

