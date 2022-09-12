number_of_companies, number_of_requests = list(map(int,input().split()))

company_number_to_location = {}

for index, location in enumerate(list(map(int,input().split()))):
    company_number = index + 1
    company_number_to_location[company_number] = location


for i in range(number_of_requests):
    request_type, *data = list(map(int,input().split()))
    if request_type == 1:
        company_number = data[0]
        new_location = data[1]
        company_number_to_location[company_number] = new_location
    else:
        company_number_one = data[0]
        company_number_two = data[1]
        company_location_one = company_number_to_location[company_number_one]
        company_location_two = company_number_to_location[company_number_two]
        distance = abs(company_location_one - company_location_two)
        print(distance)
