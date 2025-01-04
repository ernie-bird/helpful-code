def is_prime(n):
    if n < 2:
        print("Not Prime")
    elif n >= 2:
        flag = True
        for k in range (2, n):
            if n % k == 0:
                    flag = False
                    break
        if flag:
             print("Prime")
        else:
             print("Not Prime")
                    


for i in range(20):
    print(i, end=": ")
    is_prime(i)
