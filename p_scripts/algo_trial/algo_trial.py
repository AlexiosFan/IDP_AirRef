from itertools import permutations

import numpy as np
import pandas as pd
import random as rand

perm = []

def points(p):
    print("generating the polytope for p = " + str(p))

    map = {i: p.index(i) for i in p}
    pi = permutations(p)
    C = []
    for l in pi:
        perm.append(list(l))
        temp = [l[0]]
        for i in range(1, len(l)):
            temp.append(l[i] + temp[-1])
        temp2 = p.copy()
        for i in range(len(l)):
            temp2[map[l[i]]] = temp[i]
        tmp = [1/x for x in temp2.copy()]
        C.append(tmp)
    return C

def brute_force(vertices, weights):
    res = 0
    for v in vertices:
        if res == 0 or res > np.dot(v, weights):
            res = np.dot(v, weights)
            opt = v
    if res == 0:
        print("No solution")
        exit()
    return (res, opt)

def search(weights, p_time):
    perm = p_time.copy()
    direction = np.array([-w for w in weights])
    sorted = {}
    for i in range(len(weights)):
        for j in range(len(weights)):
            if(i == j):
                continue
            if (i > j):
                sorted[(p_time[i], p_time[j])] = not sorted[(p_time[j], p_time[i])]
                continue
            temp = np.zeros(len(weights))
            temp[i] = 1
            temp[j] = -1

            res = np.dot(temp, direction)
            sorted[(perm[i], perm[j])] = res < 0
    for i in range(len(weights)):
        index = i
        for j in range(i + 1, len(weights)):
            if sorted[(perm[index], perm[j])]:
                index = j
        perm[index], perm[i] = perm[i], perm[index]
    res = []
    for p in p_time:
        i = perm.index(p)
        res.append(1/sum(perm[:i + 1]))
    
    print(sorted)
    return (np.dot(np.array(res), weights), res, perm) 




weights = np.array([5, 6, 3, 9])
# [rand.randint(1, 10) for i in range(4)]
p_time = [2, 3, 4, 5]
vertices = points(p_time)

res1 = brute_force(np.array(vertices), weights)
res2 = search(weights, p_time)

# exit()
print("The brute-force solution is " + str(res1[0]))
print("The search solution is " + str(res2[0]))
print()

print("The brute-force optimal vertex is \n" + str(res1[1]))
print("The search optimal vertex is \n" + str(res2[1]))

print()
i = vertices.index(list(res1[1]))
permutation = perm[i]
print("The brute-force permutation is \n" + str(permutation))
print("The search permutation is \n" + str(res2[2]))

