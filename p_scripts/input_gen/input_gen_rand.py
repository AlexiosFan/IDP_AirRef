import subprocess
from input_gen import *

from random import randint

print("entering the script for polytope")
p = [randint(1, 100) for i in range(5)]
map = {i: p.index(i) for i in p}


# generate the result for each permutation of the input
# This may vary for each sequence, we want to see if any algebraic property may be helpful
open('./f_vector.txt', 'w').close() # clear the output per call
f_vector = open("./f_vector.txt", "a+")
script = open("./script.pl", "w")
script.write(polymake_script(points(p), p))
script.close()


# capture the output
output = subprocess.run(["polymake", "--script", "./script.pl"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
print("script called, printing f_vector")
f_vector.write("result for " + str(p) + " is \n")
f_vector.write(output + "\n")

f_vector.close()



