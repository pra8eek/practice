class Node :
    def __init__( self , num = 0 , node = None) :
        self.val = num
        self.next = node

class LinkedList :
    def __init__( self ) :
        self.top = Node()
    
    def isEmpty( self ) :
        return True if (self.top).next == None else False

    def push_front( self , num ) :
        temp = Node( num )
        temp.next = (self.top).next
        (self.top).next = temp
        print("%d inserted at the top " %num)
    
    def push_back( self , num ) :
        temp = self.top
        while ( temp.next != None ) :
            temp = temp.next
        temp.next = Node( num )
        print("%d inserted at the bottom " %num)
    
    def push_at_index( self , num , index ) :
        temp = self.top
        for i in range( index ) :
            if temp.next == None :
                print("404 Index Not Found")
                break
            temp = temp.next
        temp.next = Node( num , temp.next )
        print("%d inserted at index %d " %(num , index))
    
    def delete( self , num ) :
        if self.isEmpty() :
            print("List is empty. Delete operation failed")
            return
        temp = self.top
        dlt = False
        while ( temp.next.next != None ) :
            if ( (temp.next).val == num) :
                temp.next = (temp.next).next
                print("%d deleted from the list "%num)
                dlt = True
                break
            temp = temp.next
        if dlt == False :
            print("%d does not exist in the list"%num)
    
    def delete_at_index( self , index ) :
        if self.isEmpty() :
            print("List is empty. Delete operation failed")
            return
        temp = self.top
        dlt = True
        for i in range(index) :
            if ( temp.next == None ) :
                print("Index %d does not exist " %index)
                dlt = False
                break
        if dlt == True :
            temp.next = (temp.next).next

    def display( self ) :
        print("Displaying contents of the list :")
        temp = self.top
        while ( temp.next != None ) :
            temp = temp.next
            print ( temp.val , end =" " )
        print()
        
ll = LinkedList()
print("1. Insert at top")
print("2. Insert at bottom")
print("3. Insert at i'th index")
print("4. Delete a number")
print("5. Delete at i'th index")
print("6. Display the contents")
print("0. Exit")
print("Enter your choice")
while (True) :
    c = int(input())
    if ( c== 1) :
        ll.push_front(int(input()))    
    elif ( c== 2) :
        ll.push_back(int(input()))    
    elif ( c== 3) :
        num , index = map( int , input().split() )
        ll.push_at_index( num , index )
    elif ( c== 4) :
        ll.delete(int(input()))  
    elif ( c== 5) :
        ll.delete_at_index(int(input()))
    elif ( c== 6) :
        ll.display()
    elif ( c== 0) :
        print("Terminating program!!!")
        break
    print("--------------------------------")