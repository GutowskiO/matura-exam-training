dane = open("dane.txt", "r")
wynik = open("wynik.txt", "w")

def nwd(a, b):
    najwiekszy_wspolny_dzielnik = 0
    for c in range(1, a+1):
        if a % c == 0 and b % c == 0:
            najwiekszy_wspolny_dzielnik = c
    return najwiekszy_wspolny_dzielnik


liczba_testow = int(dane.readline())
for a in range(liczba_testow):
    linia = dane.readline().split()
    a = int(linia[0])
    b = int(linia[1])
    wynik.write(str(nwd(a, b)) + "\n")
