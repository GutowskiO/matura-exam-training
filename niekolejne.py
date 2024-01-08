liczba_testow = int(input("Wprowadz liczbe testow: "))

for a in range(liczba_testow):
    wprowadzona_liczba = int(input("Wprowadz liczbe: "))
    if (wprowadzona_liczba >= 3):
        for b in range(0, wprowadzona_liczba + 1, 2):
            print(b)
        for c in range(1, wprowadzona_liczba + 1, 2):
            print(c)
    else:
        print("NIE")