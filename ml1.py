#6 lines of code

from sklearn import tree
feature_names = ['weight' ,'texture' ]
# texture : 0-Bumpy ; 1-Smooth
features = [ [130,1] , [140,1] , [150,0] , [170,0] ]
target_names = [ 'Apple' , 'Orange']
labels =  [ 0 , 0 , 1 , 1  ]

clf = tree.DecisionTreeClassifier()
clf.fit( features , labels )
print clf.predict( [[147 , 1]] )

#Visualising the tree
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=feature_names,  
                         class_names=target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)    
graph = graphviz.Source(dot_data) 
graph.render("apples_and_oranges") 