import math

liczba_testow = int(input("Podaj liczbe testow: "))

for a in range(liczba_testow):
    liczba_gosci = int(input("Podaj liczbe gosci: "))
    liczba_ciastek_w_1_pudelku = int(input("Podaj liczbe ciastek w 1 pudelku: "))

    liczba_potrzebnych_ciastek = 0

    for b in range(liczba_gosci):
        dlugosc_zjedzenia_1_ciastka = int(input("Podaj dlugosc zjedzenia 1 ciastka przez obzartucha w sekundach: "))
        liczba_potrzebnych_ciastek += 86400//dlugosc_zjedzenia_1_ciastka
    liczba_pudelek = math.ceil(liczba_potrzebnych_ciastek/liczba_ciastek_w_1_pudelku)
    print(liczba_pudelek)