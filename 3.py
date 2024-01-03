liczba_testow = int(input("Podaj liczbe testow: "))

for a in range(liczba_testow):


    podstawa = int(input("Podaj podstawe: "))
    wykladnik = int(input("Podaj wykladnik: "))
    potega = 1

    for b in range(wykladnik):
        potega *= podstawa

    cyfra_jednosci = potega % 10
    print(cyfra_jednosci)

