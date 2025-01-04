def incr(x):
    return x+1

def decr(x):
    return x-1

def summ(x, y):
    for i in range(y):
        x = incr(x)
    return x

def subs(x, y):
    for i in range(y):
        x = decr(x)
    return x
    
def times(x, y):
    z = 0
    for i in range(x):
        z = summ(z, y)
    return z

def expo(x, y):
    z = 1
    for i in range (y):
        z = times(z, x)
    return z
    
