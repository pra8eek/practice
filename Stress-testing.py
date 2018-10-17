import numpy as np 
def test_code( cases ) :
    error = False
    for i in range( cases ) :
        n = np.random.randint(100)
        arr = np.random.randint( low = 1 , high = 100 , size = n)
        my =  my_code( n , arr )
        correct =  correct_code( n , arr )
        if ( my[0] != correct[0] or my[1] != correct[1 ] ) :
            print("You fucker, the code fails for n = %d , d = %d"%(n,d))
            print("Output should be : %d %d"%( correct[0] , correct[1] ))
            print("Your code printed : %d %d"%( my[0] , my[1] ))
            error = True
            break
    if error == False :
        print("Your code is accurate af")

        
def my_code( n  , arr ) :
    pass

def correct_code( n , arr ) :
    pass
    

print("Number of test-cases you want : ")
n = int(input())
test_code( n )