import matplotlib 
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from sklearn import linear_model

df = pd.read_csv("all_4d_9000_normalized", index_col=0)   
facets = df['facets']
vertice = df['vertice'].map(lambda x: x[1:-1].split(', ')).map(lambda x: [float(i) for i in x]).tolist()

X_test = vertice[:100]
Y_test = facets[:100] 

X_train = vertice[100:]
Y_train = facets[100:]

reg = linear_model.Ridge(alpha=0.5) 
reg.fit(X_train, Y_train)
score = reg.score(X_test, Y_test)

print(score)
