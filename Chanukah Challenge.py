x = int(input())

for i in range(x):
    data = input().split()
    setnumber = int(data[0])
    numberofdays = int(data[1])
    total_candles = 0
    for i in range(numberofdays):
        total_candles += (i+1)+1
    print(setnumber, total_candles)
