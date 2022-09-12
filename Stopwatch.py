x = int(input())

y = []

for i in range(x):
    data = int(input())
    y.append(data)


if len(y) % 2 == 0:
    count = 0
    for i in range(0,x,2):
        count += (y[i+1] - y[i])
    print(count)
else:
    print("still running")
