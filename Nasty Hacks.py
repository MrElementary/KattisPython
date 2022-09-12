import sys

x = sys.stdin.read().splitlines()
y = x[1:]

for i in y:
    a,b,c = i.split()
    a = int(a)
    b = int(b)
    c = int(c)
    if (b - c) > a:
        print("advertise")
    elif (b - c) == a:
        print("does not matter")
    elif (b - c) < a:
        print("do not advertise")
