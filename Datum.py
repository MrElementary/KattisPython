import datetime

data = list(map(int,input().split()))

day = int(data[0])
month = int(data[1])

x = datetime.datetime(2009,month,day)

print(x.strftime("%A"))
