x = input()
x = int(x)

for i in range(x):
    data = input().split()
    strips = int(data[0])
    for i in range(1, len(data)):
                   data[i] = int(data[i])
    numberofports = sum(data[1:])
    print(numberofports-(strips-1))
