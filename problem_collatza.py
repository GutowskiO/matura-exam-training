dane = open("dane.txt", "r")
wynik = open("wynik.txt", 'w')

liczba_testow = int(dane.readline())

for a in range(liczba_testow):
    s = int(dane.readline())
    n = 0
    def oblicz_xn(n, s):
        if n == 0:
            return s
        if oblicz_xn(n-1, s) % 2 != 0:
            return 3 * oblicz_xn(n-1, s) + 1
        return oblicz_xn(n-1, s) // 2

    while oblicz_xn(n, s) != 1:
        n = n + 1
    wynik.write(str(n) + "\n")
dane.close()
wynik.close()