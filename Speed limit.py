def check():
    sets = int(input())
    count = 0
    hours = 0
    for i in range(sets):
        count_two = hours
        value = input().split()
        speed = int(value[0])
        hours = int(value[1])
        count_two = hours - count_two
        count += speed*count_two
    if count != 0:
        print(count, "miles")
    else:
        return
    if sets != -1:
        check()
    else:
        return

check()
