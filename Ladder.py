import math

wall_h, angle_a = map(int,input().split())

degrees = math.radians(angle_a)

ladder = math.ceil(wall_h/(math.sin(degrees)))

print(ladder)
