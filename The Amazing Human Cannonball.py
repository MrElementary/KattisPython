import math

number_of_cases = int(input())

for i in range(number_of_cases):
    data = list(map(float,input().split()))
    velocity = data[0]
    angle = data[1]
    distance = data[2]
    lower_height = data[3]
    upper_height = data[4]

    angle_r = math.radians(angle)
    
    
    time_at_x_pos = distance / (velocity * math.cos(angle_r))
    y_pos = ((velocity * time_at_x_pos) * math.sin(angle_r)) - (0.5*(9.81*(pow(time_at_x_pos,2))))

    if y_pos > lower_height+1 and y_pos < upper_height-1:
        print("safe")
    else:
        print("not safe")
