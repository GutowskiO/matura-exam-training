def zamien_liczbe_na_napis(liczba):
    liczba_jako_napis = ""
    while liczba > 0:
        reszta = liczba % 10
        liczba = liczba // 10
        ascii = reszta + 48
        liczba_jako_napis = chr(ascii) + liczba_jako_napis
    return liczba_jako_napis


print("Test " + zamien_liczbe_na_napis(15))
def zamien_napis_na_liczbe(napis):
    liczba = 0
    for a in range(len(napis)):
        jedna_z_cyfr = ord(napis[a]) - 48
        liczba *= 10
        liczba += jedna_z_cyfr

    return liczba
print(zamien_napis_na_liczbe("123"))

