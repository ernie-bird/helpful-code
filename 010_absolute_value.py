def abs(n):
    if n >= 0:
        print(n)
    elif n < 0:
        x = 0 - n
        print(x)

abs(-5)


#------or------

def abs(n):
  if n < 0:
    n = -n
  print(n)

abs(-1)
abs(1)
