odczyt = open("dane.txt", "r")
wynik = open("wynik.txt", "w")
liczba_testow = int(odczyt.readline())

for a in range(liczba_testow):
    dane = odczyt.readline().split()
    x = int(dane[0])
    y = int(dane[1])
    z = int(dane[2])

    wiek_matki = ((-x * z) + (y * z) - y) / (-(z - 1))
    czas_trawania_ciazy = int((-(wiek_matki - x)) * 12)

    wynik.write(str(czas_trawania_ciazy) + "\n")
wynik.close()
odczyt.close()