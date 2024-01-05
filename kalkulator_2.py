rejestr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    znak = input("Podaj znak: ")
    argument1 = int(input("Podaj argument 1: "))
    argument2 = int(input("Podaj argument 2: "))

    if znak == "z":
        rejestr[argument1] = argument2
    elif znak == "+":
        print(rejestr[argument1] + rejestr[argument2])
    elif znak == "-":
        print(rejestr[argument1] - rejestr[argument2])
    elif znak == '*':
        print(rejestr[argument1] * rejestr[argument2])
    elif znak == "/":
        print (rejestr[argument1]//rejestr[argument2])
    elif znak == "%":
        print (rejestr[argument1]%rejestr[argument2])