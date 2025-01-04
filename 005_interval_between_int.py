x, y = map(int, input("Input two integers separated by comma").split(', '))
if x > y:
    x, y = y, x

for i in range(x, y+1):
    print(i)
