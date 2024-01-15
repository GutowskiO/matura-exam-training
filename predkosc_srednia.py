odczyt = open("dane.txt", "r")
zapis = open("wynik.txt", "w")
liczba_testow = int(odczyt.readline())

for a in range(liczba_testow):
    linia = odczyt.readline().split()
    v1 = int(linia[0])
    v2 = int(linia[1])

    vsr = (2 * v1 * v2) // (v1 + v2)

    zapis.write(str(vsr) + "\n")

odczyt.close()
zapis.close()