import sys
x = sys.stdin.read().splitlines()

y = x[1:]

output = 0

for i in y:
    a,b = i.split()
    a = float(a)
    b = float(b)
    sub_total = a*b
    output = output + sub_total


print(output)
