import numpy as np 
import time
def test_code( cases ) :
    error = False
    t1 , t2 , t3 = 0.0 , 0.0 , 0.0
    for i in range( cases ) :
        n  = np.random.randint(low = 20 , high = 50)
        k  = np.random.randint(low = 2 , high = 5)
        # arr = np.random.randint(low = 2 , high = 9 , size = n)
        t1  = t1 + time.time()
        old =  old_code( n , k )
        t2 =  t2 + time.time()
        new =  new_code( n , k )
        t3 = t3 + time.time()
        if old == new :
            continue
        old.sort()
        new.sort()
        for i in range(len(old)) :
            if new[i] != old[i] and error == False:
                print("Yeah fucker, the codes gave diff output for n=%d k=%d: "%(n,k))
                print("Old output was : ",old)
                print("New output printed : ", new )
                error = True
                break
   
    if error == False :
        print("Your code is didn't change at all")

    print("Time taken by the old code : %f" %(t2-t1))
    print("Time taken by the new code : %f" %(t3-t2))
        
def old_code( n , k  ) :
    m = 10**9 + 7
    if n < k*(k+1)/2 + k  :
        return -1
    elif k == 1 :
        return n
    else :
        li = []
        for i in range(k) :
            li.append( 2 + i  )
        x = n - sum(li)
        # print(x)
        for i in range( k ) :
            li[ i ] += x//k
        # print(li)
        x = n - sum(li)
        for i in range( x ) :
            li[ k-i-1 ] += 1
        # print(li)
        return li
        
def new_code( n , k  ) :
    if n < k*(k+1)/2 + k  :
        return -1

    li = [n//k]
    li*=k
    # special case : k==2
    if k == 2 :
        ll = []
        ll.append( n - (n//2 + 1) )
        ll.append( n//2 + 1 )
        return ll
    #special case - 
    elif (n//k - k//2 )!= 1 or n%k ==0 :
        for i in range( k//2 ) :
            li[ i*2 ] -= i+1
            li[ i*2 + 1 ] += i+1
        li.sort()
        for i in range(n%k) :
            li[ k - i-1 ] +=1
    else : 
        x = 0
        for i in range( k//2 -1 ) :
            li[ i*2 ] -= i+1
            li[ i*2 + 1 ] += i+1
            x = i
        li[ 2*x + 2 ] += n%k
    return li

print("Number of test-cases you want : ")
test_code( int(input()) )