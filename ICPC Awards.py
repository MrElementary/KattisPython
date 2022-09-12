teams = int(input())

uni_team = {}

for i in range(teams):
    uni,team = input().split()
    if uni in uni_team:
        continue
    else:
        uni_team[uni] = team

count = 0

for i in uni_team:
    if count < 12:
        print(i, uni_team[i])
        count += 1
    else:
        break
