data = input()

spaces = float(0)
lower = float(0)
upper = float(0)
symbols = float(0)


for char in data:
    if char == "_":
        spaces += 1
    elif char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    else:
        symbols += 1

print(spaces/len(data))
print(lower/len(data))
print(upper/len(data))
print(symbols/len(data))
        
