liczba_testow = int(input("Podaj liczbe testow: "))

for a in range(liczba_testow):
    wprowadzona_liczba = int(input("Podaj liczbe: "))
    liczba_jest_pierwsza = True

    if wprowadzona_liczba < 2:
        liczba_jest_pierwsza = False
    else:
        for b in range(2, wprowadzona_liczba):
            if wprowadzona_liczba % b == 0:
                liczba_jest_pierwsza = False
    if liczba_jest_pierwsza:
        print('TAK')
    else:
        print("NIE")