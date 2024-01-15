def oblicz_potege_iteracyjnie(podstawa, wykladnik):
    potega = 1
    for a in range(wykladnik):
        potega = podstawa * potega
    return potega

def oblicz_potege_rekurencyjnie(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    return podstawa * oblicz_potege_rekurencyjnie(podstawa, wykladnik - 1)
print(oblicz_potege_iteracyjnie(5,4))
print(oblicz_potege_rekurencyjnie(5,4))

