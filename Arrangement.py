rooms = int(input())
teams = int(input())

remain = teams % rooms

for i in range(rooms):
    stars = ""
    stars = "".join("*" * int(teams/rooms))
    if remain > 0:
        stars = stars + "*"
        remain -= 1
    print(stars)
