
while True:
    wprowadzony_znak = input("Podaj znak: ")
    liczba_1 = int(input("Wprowadz pierwsza liczbe: "))
    liczba_2 = int(input("Wprowadz druga liczbe: "))

    if (wprowadzony_znak == "+"):
        print(liczba_1 + liczba_2)
    elif (wprowadzony_znak == "-"):
        print(liczba_1 - liczba_2)
    elif (wprowadzony_znak == "*"):
        print(liczba_1 * liczba_2)
    elif (wprowadzony_znak == "/"):
        print(liczba_1 // liczba_2)
    elif (wprowadzony_znak == "%"):
        print(liczba_1 % liczba_2)