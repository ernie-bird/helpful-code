password1 = input('Password? ')
password2 = input('Repeat password? ')

while password2 != password1:
    password2 = input("doesn't match. again!")

print('All set!')
