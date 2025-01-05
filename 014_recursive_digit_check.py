def digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + digits(n/10)

digits(1234)
