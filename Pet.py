total_list = []

for i in range(0,5):
    data = list(map(int,input().split()))
    total = sum(data)
    total_list.append(total)

print(total_list.index(max(total_list))+1, max(total_list))
