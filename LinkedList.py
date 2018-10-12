class Node :
    def __init__( self , num = 0 , node = None) :
        self.val = num
        self.next = node

class LinkedList :
    def __init__( self ) :
        self.top = Node()
    
    def push_front( self , num ) :
        temp = Node( num )
        temp.next = (self.top).next
        (self.top).next = temp
    
    def push_back( self , num ) :
        temp = self.top
        while ( temp.next != None ) :
            temp = temp.next
        temp.next = Node( num )
    
    def insert_at_index( self , val , index ) :
        temp = self.top
        for i in range( index ) :
            if temp.next == None :
                print("404 Index Not Found")
                break
            temp = temp.next
        temp.next = Node( val , temp.next )


    def display( self ) :
        temp = self.top
        while ( temp.next != None ) :
            temp = temp.next
            print ( temp.val )

ll = LinkedList()
ll.push_front(4)
ll.push_back(5)
ll.push_front(3)
ll.push_front(2)
ll.push_front(1)
ll.insert_at_index(10, 2)
ll.display()