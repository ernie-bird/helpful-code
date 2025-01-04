num = int(input("Input positive decimal integer that will turn into binary:"))
print("Decimal:", num)

bin_list = []
while num > 0:
    remainder = num % 2
    bin_list.append(remainder)
    num = num//2

print(bin_list)

rev_list = bin_list[::-1]

result = "".join(str(i) for i in rev_list)

print(result)
