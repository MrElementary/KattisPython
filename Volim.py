starter = int(input())
questions = int(input())

timer = 210

for i in range(questions):
    data = input().split()
    time_taken = int(data[0])
    outcome = data[1]
    timer -= time_taken
    if timer > 0:
        if outcome == "T":
            if starter <= 7:
                starter += 1
            else:
                starter = 1


print(starter)
