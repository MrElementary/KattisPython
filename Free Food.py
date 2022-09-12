events = int(input())

temp_list = []

for i in range(events):
    first_day, last_day = map(int,input().split())
    for x in range(first_day, last_day+1):
        temp_list.append(x)

print(len(set(temp_list)))
