width = int(input())
number_of_pieces = int(input())
total_area = 0

for i in range(number_of_pieces):
    data = list(map(int,input().split()))
    total_area += (data[0] * data[1])

print(int(total_area/width))
