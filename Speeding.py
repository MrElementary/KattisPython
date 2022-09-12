import math

photos = int(input())

temp_val_three = 0
speed = 0

temp_val_one = 0
temp_val_two = 0


for i in range(photos):
    data = input().split()
    hours = int(data[0])
    distance = int(data[1])
    temp_val_one = hours - temp_val_one
    temp_val_two = distance - temp_val_two
    if temp_val_one != 0:
        speed = temp_val_two/temp_val_one
    if temp_val_three < speed:
        temp_val_three = speed
    temp_val_one = hours
    temp_val_two = distance

print(math.floor(temp_val_three))
