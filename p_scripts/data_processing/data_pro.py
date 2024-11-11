import numpy as np
import pandas as pd 

df10k = pd.read_csv("all_4d_10k_normalized", index_col=0)
print(df10k.head())

exit()

df1k = pd.read_csv("all_4d_1000_normalized")
df9k = pd.read_csv("all_4d_9000_normalized")
df10k =  pd.concat([df1k, df9k],ignore_index=True)
df10k.to_csv("all_4d_10k_normalized")

exit()

df = pd.read_csv("all_4d_9000_sorted", index_col=0)   
df = df[df['f_vector'].map(lambda x: len(x.split(' ')) == 4)]
facets = df['f_vector'].map(lambda x: int(x.split(' ')[3]))
vertice = df['vertice'].map(lambda x: x[1:-1].split(', ')).map(lambda x: sorted([int(i) for i in x]))
normalized_vertice = vertice.map(lambda x: [a / x[0] for a in x]) 

res = pd.DataFrame(data = {'vertice': normalized_vertice, 'facets': facets})
res.to_csv("all_4d_9000_normalized")