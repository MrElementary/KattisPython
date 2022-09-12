number_of_sets = int(input())

for i in range(number_of_sets):
    output = 0
    data = input().split()
    set_number = data[0]
    base = int(data[1])
    value = int(data[2])
    temp_div = 0
    temp_mod = 0
    temp_mod_list = []
    temp_val = value
    while temp_val >= 1:
        temp_div = temp_val/base
        temp_mod = temp_val % base
        temp_mod_list.append(int(temp_mod))
        temp_val = temp_div
    for val in temp_mod_list:
        output += val * val
    print(set_number, output)
