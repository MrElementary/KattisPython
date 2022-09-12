test_cases = int(input())

value = list()

for i in range(test_cases):
    number_of_shops = int(input())
    shop_location = list(map(int,input().split()))
    furthest_location = max(shop_location)
    closest_location = min(shop_location)
    walking_distance = (furthest_location - closest_location) * 2
    print(walking_distance)
