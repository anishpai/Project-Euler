#PROJECT EULER
#P15: Lattice paths

#Solved using permutation and combination(https://math.stackexchange.com/questions/286437/arrangement-of-binary-bits)

import math
from math import factorial
n=0
paths =0
def num_grid(n):
    paths = factorial(n*2) / (factorial(n)**2)
    print(paths)

print("The number of paths in 20x20 grid are:")
num_grid(20)
