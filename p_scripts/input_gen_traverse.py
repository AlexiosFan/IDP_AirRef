import subprocess
from input_gen import *

import numpy as np
import pandas as pd

vertices = []
f_vectors = []

l = [4, 8, 16, 32]

for p in [[a, b, c, d, e, f] for a in l for b in l for c in l for d in l for e in l for f in l]:
    map = {i: p.index(i) for i in p}

    # generating the script
    script = open("./script.pl", "w")
    script.write(polymake_script(points(p), p))
    script.close()


    # capture the output
    output = subprocess.run(["polymake", "--script", "./script.pl"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
    vertices.append(str(p))
    f_vectors.append(output)

df = pd.DataFrame(data = {'vertice': vertices, 'f_vector': f_vectors})

df.to_csv("all_6d_16")