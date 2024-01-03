liczba_testow = int(input("Podaj liczbe testow: "))

for a in range(liczba_testow):
    grupa_1 = int(input('Podaj liczbe dzieci w gr 1: '))
    grupa_2 = int(input("Podaj liczbe dzieci w gr 2: "))
    NWW = 1

    while NWW % grupa_1 != 0 or NWW % grupa_2 != 0:
       NWW += 1

    print(NWW)