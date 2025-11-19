import itertools
from random import choice
# ZADANIE 7.6


#a)
a = itertools.cycle(range(0,2))

#b)
b = (choice(['N', 'E', 'W', 'S']) for i in iter(int, 1))

#c)
c = a = itertools.cycle(range(0,7))

limit_for_all = 10 # ile pierwszych wyrazow ciagu wydrukować
def print_iter(obj, nr_zad, limit):
    print(f"Zadanie {nr_zad} (pierwsze {limit}):")
    j = 0
    for i, element in enumerate(obj):
        print(element)
        if i > limit:
            break
print_iter(a, "A", limit_for_all)
print_iter(b, "B", limit_for_all)
print_iter(c, "C", limit_for_all)