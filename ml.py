from sklearn import tree
# features - [weight,texture]
# texture : 0-Bumpy ; 1-Smooth
features = [ [130,1] , [140,1] , [150,0] , [170,0] ]
# labels : 0-Apple ; 1-Orange
labels =  [ 0 , 0 , 1 , 1 , 2 , 2 ]

clf = tree.DecisionTreeClassifier()
clf = clf.fit( features , labels )
print clf.predict( [[150 , 0]] )