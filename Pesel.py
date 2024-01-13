odczyt = open("dane.txt", "r")
wynik = open("wynik.txt", "w")

liczba_testow = int(odczyt.readline())
for a in range(liczba_testow):
    przyjety_pesel = odczyt.readline().strip()
    poprawnosc_pesela = False
    suma_iloczynow_cyfr_peselu = 0
    for b in range(len(przyjety_pesel)):
        przyjeta_wartosc = int(przyjety_pesel[b])
        if b == 0 or b == 4 or b == 8 or b ==10:
            dodana_liczba_do_sumy = przyjeta_wartosc
        elif b == 1 or b == 5 or b == 9:
            dodana_liczba_do_sumy = przyjeta_wartosc * 3
        elif b == 2 or b == 6:
            dodana_liczba_do_sumy = przyjeta_wartosc * 7
        else:
            dodana_liczba_do_sumy = przyjeta_wartosc * 9

        suma_iloczynow_cyfr_peselu = suma_iloczynow_cyfr_peselu + dodana_liczba_do_sumy
    if suma_iloczynow_cyfr_peselu > 0 and suma_iloczynow_cyfr_peselu % 10 == 0:
        poprawnosc_pesela = True
    if (poprawnosc_pesela):
        wynik.write("D \n")
    else:
        wynik.write("N \n")
