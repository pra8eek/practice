class Node :
    def __init__( self , num = 0 , node = None) :
        self.val = num
        self.next = node

class LinkedList :
    def __init__( self ) :
        self.top = Node()
        self.count = 0
    
    def isEmpty( self ) :
        return True if (self.top).next == None else False

    def insert_at_front( self , num ) :
        temp = Node( num )
        temp.next = (self.top).next
        (self.top).next = temp
        self.count = self.count + 1
        print("%d inserted at the top " %num)
    
    def insert_at_back( self , num ) :
        temp = self.top
        while ( temp.next != None ) :
            temp = temp.next
        temp.next = Node( num )
        self.count = self.count + 1
        print("%d inserted at the bottom " %num)
    
    def insert_at_index( self , num , index ) :
        temp = self.top
        for i in range( index ) :
            if temp.next == None :
                print("404 Index Not Found")
                return
            temp = temp.next
        temp.next = Node( num , temp.next )
        self.count = self.count + 1
        print("%d inserted at index %d " %(num , index))
    
    def delete( self , num ) :
        if self.isEmpty() :
            print("List is empty. Delete operation failed")
            return
        temp = self.top
        dlt = False
        while ( temp.next != None ) :
            if ( (temp.next).val == num) :
                temp.next = (temp.next).next
                print("%d deleted from the list "%num)
                self.count = self.count - 1
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
            temp = temp.next
        if dlt == True :
            self.count = self.count - 1
            print("Index %d with value %d deleted from the list "%( index , (temp.next).val ))
            temp.next = (temp.next).next
    
    def delete_front( self ) :
        self.delete_at_index(0)
    
    def delete_back( self ) :
        self.delete_at_index( self.count - 1 )

    def display( self ) :
        if self.isEmpty() :
            print("The list is empty") 
            return
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
print("6. Delete at top")
print("7. Delete at bottom")
print("8. Count number of elements")
print("9. Display the contents")
print("0. Exit")
print("Enter your choice")
while (True) :
    c = int(input())
    if ( c== 1) :
        print("Enter the number to be inserted at top : ",end=' ')
        ll.insert_at_front(int(input()))    
    elif ( c== 2) :
        print("Enter the number to be inserted at bottom : ",end=' ')
        ll.insert_at_back(int(input()))    
    elif ( c== 3) :
        print("Enter the number and the index where you want add : ",end=' ')
        try :
            num , index = map( int , input().split() )
            ll.insert_at_index( num , index )
        except ValueError :
            print("You were supposed to enter 2 space separated arguments. Number and Index")
            print("Try again : ", end=" ")
            try :
                num , index = map( int , input().split() )
                ll.insert_at_index( num , index )
            except ValueError :
                print("You crazy or what!! Can't you understand what 2 numbers mean!!!")
                print("Here's your last try : " , end=' ')
                try :
                    num , index = map( int , input().split() )
                    ll.insert_at_index( num , index )
                except :
                    print("You know what, FUCK OFF!")
                    print("Aborting program. Take care you psychopath")
                    break
    elif ( c== 4) :
        print("Enter the number to be deleted : ",end=' ')
        ll.delete(int(input()))  
    elif ( c== 5) :
        print("Enter the index to be deleted : ",end=' ')
        ll.delete_at_index(int(input()))
    elif ( c == 6 ) :
        ll.delete_front()
    elif ( c == 7 ) :
        ll.delete_back()
    elif ( c == 8 ) :
        print("Number of elements int he list are %d" %ll.count)
    elif ( c== 9) :
        ll.display()
    elif ( c== 0) :
        print("Terminating program!!!")
        break
    print("--------------------------------")