x = input()
data = map(int,input().split())
total = 0
for i in data:
    if i < 0:
        total += 1
print(total)
