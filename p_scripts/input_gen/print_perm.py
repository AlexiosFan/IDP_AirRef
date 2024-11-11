from itertools import permutations

p = [1, 2, 3, 4]

map = {i: p.index(i) for i in p}
pi = permutations(p)

C = []
for l in pi:
    temp = [l[0]]
    for i in range(1, len(l)):
        temp.append(l[i] + temp[-1])
    temp2 = p.copy()
    for i in range(len(l)):
        temp2[map[l[i]]] = temp[i]
    C.append(temp2.copy())

C1 = sorted(C, key=lambda x: (x[0]))
C2 = sorted(C, key=lambda x: (x[1]))
C3 = sorted(C, key=lambda x: (x[2]))
C4 = sorted(C, key=lambda x: (x[3]))

for c in C1:
    print(c)
print()
for c in C2:
    print(c)
print()
for c in C3:
    print(c)
print()
for c in C4:
    print(c)