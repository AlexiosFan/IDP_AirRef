from itertools import permutations
from math import prod

print("entering the script for polytope")
p = [10, 34, 5, 20]
map = {i: p.index(i) for i in p}



print("generating the polytope for p = " + str(p))

pi = permutations(p)
C = []
Values = []
for l in pi:
    temp = [l[0]]
    for i in range(1, len(l)):
        temp.append(l[i] + temp[-1])
        Values.append(l[i] + temp[-1])
    temp2 = p
    for i in range(len(l)):
        temp2[map[l[i]]] = temp[i]
    C.append(temp2.copy())

lcm = prod(list(set(p)))

C_inv = [[str(int(lcm / x)) for x in c] for c in C]
C_inv_str = 'Names:\n'
C_inv_str += ' '.join(['x'+str(x) for x in range(len(p) - 1)]) + ' \n'
C_inv_str += '\nVertices:\n'
for l in C_inv:
    length = len(l)
    C_inv_str += '' + l[0]
    for i in range(1, length-1):
        C_inv_str += ' ' + l[i]
    C_inv_str += ' \n'

C_inv_str += ''

print("points generated, calling the scipt")

points = open("./points.txt", "w")
points.write(C_inv_str) 
points.close()