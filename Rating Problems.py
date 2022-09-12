number_of_judges, number_of_prerateds = list(map(int,input().split()))

rating = 0

unrated_judges = number_of_judges - number_of_prerateds

for i in range(number_of_prerateds):
    rating += int(input())


max_rating = (rating + (unrated_judges * 3)) / number_of_judges
min_rating = (rating - (unrated_judges * 3)) / number_of_judges

print(min_rating, max_rating)
