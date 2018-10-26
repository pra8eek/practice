import numpy as np 
import time
def test_code( cases ) :
    error = False
    t1 , t2 , t3 = 0.0 , 0.0 , 0.0
    for i in range( cases ) :
        n  = np.random.randint(low = 2 , high = 5)
        # k  = np.random.randint(low = 2 , high = 9)
        arr = np.random.randint(low = 2 , high = 9 , size = n)
        t1  = t1 + time.time()
        old =  old_code( n , k , list(arr) )
        t2 =  t2 + time.time()
        new =  new_code( n , k , list(arr) )
        t3 = t3 + time.time()
        if ( old != new ) :
            print("Yeah fucker, old code failed for n = %d , k = %d and array : "%(n,k))
            print(arr)
            print("Old output was : %s"%( old ))
            print("New output printed : %s"%( new ))
            error = True
            break
   
    if error == False :
        print("Your code is didn't change at all")
    print("Time taken by the old code : %f" %(t2-t1))
    print("Time taken by the new code : %f" %(t3-t2))

        
def old_code( n , k , b ) :
    b.sort()
    for i in range(n-1):
        while(b[i] > k):
            b[i] -= 1
            b[i+1] -= 1
    return sum(b)
            
def new_code( n , k , arr ) :
    arr.sort()
    while ( arr[n-2] > k ) :
        for j in range ( n-2 , 1 , -1 ) :
            if arr[ j ] > k :
                arr[j] -= 1
                arr[j-1] -= 1
        arr.sort()
    return (sum(arr))
    

print("Number of test-cases you want : ")
test_code( int(input()) )