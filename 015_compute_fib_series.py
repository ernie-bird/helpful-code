def fib (n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    elif n > 1:
        n = fib(n-1)+fib(n-2)
        return n
    
fib(7)    
