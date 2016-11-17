# How many such routes are there through a 20x20 grid?

import euler

def lattice_patterns(n):
    points = n + 1
    first_row=[]
    second_row=[]
    for i in range(0,points):
        first_row.append(1)
    print(first_row)


print(euler.factorial(5))
lattice_patterns(2)
