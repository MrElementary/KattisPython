test_cases = int(input())

for i in range(test_cases):
    number_of_visits = int(input())
    places = set()
    for i in range(number_of_visits):
        city = input()
        places.add(city)
    print(len(places))
            
