liczba_testow = int(input("Podaj liczbe testow: "))

for a in range(liczba_testow):
    tablica = []
    tablica_po_uporzadkowaniu = []
    liczba_elementow_w_tablicy = int(input("Podaj liczbe elementow w tablicy: "))
    for b in range(liczba_elementow_w_tablicy):
        element_tablicy = int(input("Podaj element tablicy: "))
        tablica.append(element_tablicy)
    for c in range(1, liczba_elementow_w_tablicy):
        if (c+1) % 2 == 0:
            tablica_po_uporzadkowaniu.append(tablica[c])
    for d in range(liczba_elementow_w_tablicy):
        if (d+1) % 2 != 0:
            tablica_po_uporzadkowaniu.append(tablica[d])
    print(tablica_po_uporzadkowaniu)

