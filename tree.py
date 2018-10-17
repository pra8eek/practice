class Node :
    def __init__( self , num = 0 ) :
        self.val = num
        self.left = None
        self.right = None
class Tree :
    def __init__( self , num = 0) :
        self.root = Node( num )
    