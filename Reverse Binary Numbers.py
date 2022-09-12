x = int(input())

y = bin(x).replace("0b", "")

reverse_y = int(str(y)[::-1],2)

print(reverse_y)


