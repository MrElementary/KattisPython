
value = ''

while value != '0':
    split_val_one = 0
    split_val_two = 0
    counter = 11
    value = input()
    if value == '0':
        break
    for i in value:
        i = int(i)
        split_val_one += i
    value_two = counter * int(value)
    value_two = str(value_two)
    for i in value_two:
        i = int(i)
        split_val_two += i
    while split_val_one != split_val_two:
        split_val_two = 0
        counter += 1
        value_two = counter * int(value)
        value_two = str(value_two)
        for i in value_two:
            i = int(i)
            split_val_two += i
    print(counter)
    
