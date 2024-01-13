while True:
    n = int(input("Podaj zmienna n: "))
    x = int(input("Podaj liczbe, przez ktora liczba musi byc podzielna: "))
    y = int(input("Podaj liczbe, przez ktora liczba nie moze byc podzielna: "))

    for a in range(n):
        if (a % x == 0 and a % y != 0):
            print(a)
