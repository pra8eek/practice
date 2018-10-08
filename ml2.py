import numpy as np
import graphviz
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()

# print iris.feature_names
# print iris.target_names
# print iris.data[3] , iris.target[3]

remove = [0,50,100]
train_target = np.delete( iris.target , remove )
train_data = np.delete( iris.data , remove , axis = 0)
test_target = iris.target[ remove ]
test_data = iris.data[ remove ]

clf = tree.DecisionTreeClassifier() 
clf.fit( train_data , train_target)

print test_target
print clf.predict( test_data )

#Visualising the tree