import datetime

cases = int(input())

for i in range(cases):
    rating = "ineligible"
    data = list(map(str,input().split()))
    name = data[0]
    study_date = data[1]
    birth_date = data[2]
    courses = int(data[3])
    study_date = datetime.datetime.strptime(study_date, '%Y/%m/%d')
    birth_date = datetime.datetime.strptime(birth_date, '%Y/%m/%d')
    study_date = study_date.year
    birth_date = birth_date.year
    if study_date >= 2010:
        rating = "eligible"
    if birth_date >= 1991:
        rating = "eligible"
    if rating == "ineligible":
        if courses/5 <= 8:
            rating = "coach petitions"
    print(name, rating)    
