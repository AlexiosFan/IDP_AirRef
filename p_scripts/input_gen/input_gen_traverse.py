import subprocess
from input_gen import *

import numpy as np
import pandas as pd
import random as rand

vertices = []
f_vectors = []

for i in range(9000):
    p = []
    for j in range(4):
        x = rand.randint(1, 1000)
        p.append(x)

    # generating the script
    script = open("./script.pl", "w")
    script.write(polymake_script(points(p), p))
    script.close()


    # capture the output
    output = subprocess.run(["polymake", "--script", "./script.pl"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
    vertices.append(str(p))
    f_vectors.append(output)

df = pd.DataFrame(data = {'vertice': vertices, 'f_vector': f_vectors})
df.to_csv("all_4d_9000_sorted")