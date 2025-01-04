sent = input("Input sentence:")

count_e = 0
count_E = 0
for i in sent:
    if i == 'e':
        count_e += 1
    elif i == 'E':
        count_E += 1

        
print(f"\"{sent}\" has E {count_E}, e {count_e}, together {count_E+count_e}")
