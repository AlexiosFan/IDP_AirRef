import numpy as np
import pandas as pd
import graphviz

df = pd.read_csv("all_4d_1000_normalized", index_col=0)   
# facets = df['f_vector'].map(lambda x: int(x.split(' ')[3])).tolist()
# vertice = df['vertice'].map(lambda x: x[1:-1].split(', ')).map(lambda x: [int(i) for i in x]).tolist()

facets = df['facets']
vertice = df['vertice'].map(lambda x: x[1:-1].split(', ')).map(lambda x: [float(i) for i in x]).tolist()

X_test = vertice[:100]
Y_test = facets[:100] 

X_train = vertice[100:]
Y_train = facets[100:]

from sklearn import linear_model, tree, ensemble

DT = tree.DecisionTreeClassifier()
LR = linear_model.LogisticRegression()
RF = ensemble.RandomForestClassifier()

DT.fit(X_train, Y_train)
LR.fit(X_train, Y_train)
RF.fit(X_train, Y_train)

print(DT.score(X_test, Y_test)) 
print(LR.score(X_test, Y_test))
print(RF.score(X_test, Y_test))

tree.export_graphviz(DT, out_file="DT_VIS") 

exit()

df = pd.read_csv("all_4d_1000", index_col=0)   
Y_test_new = df['f_vector'].map(lambda x: int(x.split(' ')[3])).tolist()
X_test_new = df['vertice'].map(lambda x: x[1:-1].split(', ')).map(lambda x: [int(i) for i in x]).tolist()

print(LR.score(X_test_new, Y_test_new))