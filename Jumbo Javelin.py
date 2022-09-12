import sys

x = sys.stdin.read().splitlines()

y = x[1:]

total = 1

for i in y:
    total = (total + int(i)) - 1

print(total)
