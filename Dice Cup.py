data = input().split()

x = int(data[0])
y = int(data[1])

mini = min(x, y)
maxi = max(x, y)

for i in range(mini, maxi+1):
    print(i+1)
