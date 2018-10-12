class Node :
    def __init__( self , num = 0) :
        self.val = num
        self.next = 0

class LinkedList :
    def __init__( self ) :
        self.top = Node()
    
    def push_front( self , num ) :
        temp = Node( num )
        temp.next = (self.top).next
        (self.top).next = temp

    def display( self ) :
        temp = self.top
        while ( temp.next != 0 ) :
            temp = temp.next
            print ( temp.val )

ll = LinkedList()
ll.push_front(5)
ll.push_front(7)
ll.push_front(2)
ll.push_front(8)
ll.display()