def sprawdz_znak_liczb(indeks, liczby):
    if indeks >= len(liczby):
        return
    if liczby[indeks] == "0":
        print("zero")
        return sprawdz_znak_liczb(indeks + 2, liczby)
    if liczby[indeks] == "-":
        print("ujemne")
        return sprawdz_znak_liczb(indeks + 3, liczby)
    else:
        print("dodatnie")
        return sprawdz_znak_liczb(indeks + 2, liczby)


liczby = str(input("Podaj cyfry: "))
indeks = 0
sprawdz_znak_liczb(indeks, liczby)
