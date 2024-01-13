odczyt = open("dane.txt", "r")
wynik = open("wynik.txt", "w")

liczba_testow = int(odczyt.readline())
for a in range(liczba_testow):
    otrzymany_string = odczyt.readline()
    dlugosc_polowy_stringa = len(otrzymany_string) // 2
    polowa_stringa = ""
    for b in range(dlugosc_polowy_stringa):
        polowa_stringa = polowa_stringa + otrzymany_string[b]
    wynik.write(polowa_stringa + "\n")


