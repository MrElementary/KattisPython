import math

side_one, side_two, side_three, side_four = map(int,input().split())

length = (side_one + side_two + side_three + side_four) / 2

answer = math.sqrt((length - side_one)*(length - side_two)*(length - side_three)*(length - side_four))

print(answer)
