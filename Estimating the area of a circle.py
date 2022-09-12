import math

def input_calc():
    data = list(map(float,input().split()))
    radius = data[0]
    total_dots = data[1]
    dots_inside = data[2]
    if radius == 0:
        return
    else:
        ratio_val = (dots_inside/total_dots)
        area_of_sq = pow((radius*2),2)
        estimate_of_circle = area_of_sq * ratio_val
        print("{:.5f} {:.5f}".format(math.pi*(radius*radius), estimate_of_circle))
        input_calc()

input_calc()
