items, days = map(int,input().split())

item_list = []
count = 0

while len(item_list) <= items:
    item = input()
    count += 1
    if item not in item_list:
        item_list.append(item)
    if len(item_list) == items:
        print(count)
        break
    if count == days:
        if days == items:
            if len(item_list) < items:
                print("paradox avoided")
                break
            else:
                print(count)
                break
        elif len(item_list) < items:
            print("paradox avoided")
            break
        else:
            print("paradox avoided")
            break
