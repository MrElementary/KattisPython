boxes = int(input())

count = 0

for i in range(boxes):
    box_name = str.lower(input())
    if "rose" in box_name or "pink" in box_name:
        count += 1
        

if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")

        
