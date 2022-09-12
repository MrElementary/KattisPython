numbers = int(input())

values = list(map(int,input().split()))

count = 0

for i in values:
    if i < 0:
        count -= i

print(count)
