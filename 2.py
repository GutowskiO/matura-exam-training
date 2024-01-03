liczba_testow = int(input('Podaj liczbę testów: '))

for a in range(liczba_testow):
    liczba = int(input("Podaj liczbę: "))

    silnia = 1
    for b in range(2,liczba + 1):
        silnia *= b

    liczba_jednosci = silnia % 10
    liczba_dziesiatek = silnia//10 % 10

    print(liczba_dziesiatek)
    print(liczba_jednosci)