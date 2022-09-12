x = float(input())
y = int(input())

total_cost = 0

for i in range(y):
    data = input().split()
    width = float(data[0])
    length = float(data[1])
    sizeoflawn = width*length
    costoflawn = sizeoflawn*x
    total_cost = total_cost + costoflawn

print(round(total_cost,8))
