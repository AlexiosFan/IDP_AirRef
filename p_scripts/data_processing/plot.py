import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

df10k = pd.read_csv("all_4d_10k_normalized", index_col=0)
vertices = df10k['vertice'].map(lambda x: x[1:-1].split(', ')).map(lambda x: [float(i) for i in x[1:]])
facets = df10k['facets']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

plotted_v = vertices[:1000]
plotted_f = facets[:1000]

xs = [v[0] for v in plotted_v]
ys = [v[1] for v in plotted_v]
zs = [v[2] for v in plotted_v]

ax.scatter(xs, ys, zs, c=plotted_f, cmap='viridis', s=50, alpha=0.6)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()