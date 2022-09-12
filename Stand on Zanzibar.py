x = int(input())

count = 0

for i in range(x):
    data = list(map(int,input().split()))
    data_2 = list()
    for k in range(len(data)-2):
        if data[k+1] - data[k] > data[k]:
            data_2.append(data[k+1] - (data[k]*2))
        else:
            continue
    print(sum(data_2))


