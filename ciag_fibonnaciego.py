def ciag_fibonnaciego_iteracyjnie(element):
    element_ciagu = 0
    liczba = 1
    poprzednia_liczba = 1
    if element == 1:
        return 0
    if element == 2 or element == 3:
        return 1
    for a in range(4, element + 1):
        element_ciagu = liczba + poprzednia_liczba
        poprzednia_liczba = liczba
        liczba = element_ciagu
    return element_ciagu

def ciag_fibonnaciego_rekurencyjnie(element):
    if element == 1:
        return 0
    if element == 2 or element == 3:
        return 1
    return ciag_fibonnaciego_iteracyjnie(element - 1) + ciag_fibonnaciego_rekurencyjnie(element - 2)

print(ciag_fibonnaciego_rekurencyjnie(14))
print(ciag_fibonnaciego_iteracyjnie(14))



