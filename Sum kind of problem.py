numberofsets = int(input())

for i in range(numberofsets):
    data = input().split()
    set_value = data[0]
    value = int(data[1])
    first_sum = 0
    second_sum = 0
    third_sum = 0
    for i in range(0,value+1):
        first_sum += i
    for i in range(0, value*2+1,2):
        second_sum += i
    for i in range(1, value*2+1,2):
        third_sum += i
    print(set_value, first_sum, third_sum, second_sum)
