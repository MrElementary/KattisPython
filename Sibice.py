import math

matches, width, height = map(int,input().split())

diagonal = math.sqrt((pow(width,2)+pow(height,2)))

for i in range(matches):
    match_length = int(input())
    if match_length <= width or match_length <= height or match_length <= diagonal:
        print("DA")
    else:
        print("NE")
