data = input().split()
item_data = input().split()

total_item_weight = 0

for i in range(0, len(item_data)):
    item_data[i] = int(item_data[i])
    total_item_weight += item_data[i]
    
grossweight = int(data[0])
truckweight = int(data[1])

max_weight = ((grossweight-truckweight)*0.9)-total_item_weight

print(int(max_weight))
