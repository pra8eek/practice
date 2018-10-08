import numpy as np
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
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names = iris.feature_names,  
                         class_names = iris.target_names,  
                         filled = True, rounded = True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
