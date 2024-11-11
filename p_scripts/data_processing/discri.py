import numpy as np
import pandas as pd

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

df = pd.read_csv("all_4d_1000_normalized", index_col=0)   

# consider only two classes
df = df[(df ['facets'] == 68) | (df['facets'] == 70) ] 

facets = df['facets']
vertice = df['vertice'].map(lambda x: x[1:-1].split(', ')).map(lambda x: [float(i) for i in x]).tolist()

# class_68_70 = facets.filter(lambda x: x == 68 or x == 70)
# vertice_68_70 = vertice[class_68_70.index]

X_test = vertice[:100]
Y_test = facets[:100] 

X_train = vertice[100:]
Y_train = facets[100:]


clf = QuadraticDiscriminantAnalysis() 
clf.fit(X_train, Y_train)
score = clf.score(X_test, Y_test)

print(score)
print(clf.get_params(deep=True))