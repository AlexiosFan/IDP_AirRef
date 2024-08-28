from itertools import permutations
import subprocess

print("entering the script for polytope")

# generate all points given a sequence of points
def points(p):
    print("generating the polytope for p = " + str(p))

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

    C_inv = [["1/" + str(x) for x in c] for c in C]
    C_inv_str = '['

    for l in C_inv:
        length = len(l)
        C_inv_str += '[1, ' + l[0]
        for i in range(1, length):
            C_inv_str += ', ' + l[i]
        C_inv_str += '], '

    C_inv_str = C_inv_str[:-2]
    C_inv_str += ']'
    return C_inv_str

# string for the polymake script
def polymake_script(points, p):
    print("script generated for " + str(p) + ", calling the scipt")
    script = """
            use application "polytope";
            my $p = new Polytope(POINTS=>""" + points + """); \n
            print $p->F_VECTOR;
            """
    return script

# generate the result for each permutation of the input
# This may vary for each sequence, we want to see if any algebraic property may be helpful
# open('./f_vector.txt', 'w').close() # clear the output per call
# f_vector = open("./f_vector.txt", "a+")
# script = open("./script.pl", "w")
# script.write(polymake_script(points(p), p))
# script.close()


# capture the output
# output = subprocess.run(["polymake", "--script", "./script.pl"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
# print("script called, printing f_vector")
# f_vector.write("result for " + str(p) + " is \n")
# f_vector.write(output + "\n")

# f_vector.close()



