def prime(x):
    for i in range(2, x+1):
        prime_num = True
        for j in range(2, i):
            if i % j == 0:
                prime_num = False
                break
        if prime_num:
            print(i)

prime(30)
