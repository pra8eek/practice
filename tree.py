from sklearn import tree
class Node :
    def __init__( self , num = None ) :
        self.val = num
        self.left = None
        self.right = None
class Tree :
    def __init__( self , num = None ) :
        self.root = Node(num)

    def isEmpty( self ) :
        return True if self.root.val == None else False

    def insert(self , num , node = None) :
        if self.isEmpty() :
            self.root.val = num 
            print("%d inserted successfully"%num)
            return
        if node == None :
            node = self.root
        if num < node.val :
            if node.left == None :
                node.left = Node(num) 
                print("%d inserted successfully"%num)
            else :
                self.insert( num , node.left )
        elif num > node.val :
            if node.right == None :
                node.right = Node(num) 
                print("%d inserted successfully"%num)
            else :
                self.insert( num , node.right )
        else :
            print("Element already present!!! , Insertion Failed")

    def traverse(self , n) :
        if n == 1 :
            self.Preorder(self.root)
            print()
        elif n == 2 :
            self.Inorder(self.root) 
            print()
        elif n==3 :
            self.Postorder(self.root)
            print()
        else :
            print("MUH ME LOGE!!")
    
    def Preorder(self , node) :
        if node == None :
            return
        else :
            print(node.val , end= " ")
            self.Preorder(node.left)
            self.Preorder(node.right)
    def Inorder(self , node) :
            if node == None :
                return
            else :
                self.Inorder(node.left)
                print(node.val , end= " ")
                self.Inorder(node.right)
    def Postorder(self , node) :
            if node == None :
                return
            else :
                self.Postorder(node.left)
                self.Postorder(node.right)
                print(node.val , end= " ")

tt = Tree()
tt.insert(5)
tt.insert(3)
tt.insert(7)
tt.insert(2)
tt.insert(6)
tt.insert(9)
print("1. Insert")
print("2. Preorder Traversal")
print("3. Inorder Traversal")
print("4. Postorder Traversal")
print("0. Exit")
n = -1
while n!=0 :
    n = int(input()) 
    if n == 0 :
        print("Sad that you quit, cuz that's what losers do bitch")
        break
    elif n == 1 :
        print("Enter the value to be inserted : ",end="")
        tt.insert(int(input()))
    elif n == 2 :
        tt.traverse(n-1)
    elif n == 3 :
        tt.traverse(n-1)
    elif n == 4 :
        tt.traverse(n-1)
    else :
        print("Chutiya hai kya! Fir se daal")
    print("-----------------------------------------------------------")
