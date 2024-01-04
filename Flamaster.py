dane = open("dane.txt", "r")
wynik = open("wynik.txt", "w")

liczba_testow = int(dane.readline())
for a in range(liczba_testow):
    linia = dane.readline()
    for litera in linia:
        liczba_wystapien_litery = 0
        for b in range(len(linia)):
            if linia[b] == litera:
                liczba_wystapien_litery += 1
        if liczba_wystapien_litery > 2:
            ciag_liter_do_zamiany = ''
            for c in range(liczba_wystapien_litery):
                ciag_liter_do_zamiany = ciag_liter_do_zamiany + litera
            linia = linia.replace(ciag_liter_do_zamiany, litera + str(liczba_wystapien_litery))
    wynik.write(linia)
