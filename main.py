liczba_testow = int(input("Podaj liczbe testow: "))


for a in range(liczba_testow):
    suma_liczb = 0
    liczba_liczb_do_smuowania = int(input("Podaj liczbe liczb: "))
    for b in range(liczba_liczb_do_smuowania):
        wpisana_liczba = int(input("Podaj liczbe: "))

        suma_liczb = suma_liczb + wpisana_liczba
    print(suma_liczb)






