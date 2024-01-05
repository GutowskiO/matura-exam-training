liczba_partii = int(input("Podaj liczbe partii: "))

for a in range(liczba_partii):
    zetony_a = int(input("Podaj liczbe zetonow gracza a: "))
    zetony_b = int(input("Podaj liczbe zetonow gracza b: "))

    while zetony_a != zetony_b:
        if zetony_a > zetony_b:
            zetony_a -= zetony_b
        else:
            zetony_b -= zetony_a

    print(zetony_a + zetony_b)
