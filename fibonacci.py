def fib(n):
    if n <= 0:
        print("Input must be a positive integer.") #if n is negative or 0
        return
    
    a = 0
    b = 1 
    
    if n == 1:
        print(a)  #if n is 1
        return
    else: 
        print(a)
        print(b)
        
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fib(5)  
