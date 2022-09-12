blimps = 5

data = []

for i in range(blimps):
    data.append(input())

answer = ""

for i in range(len(data)):
    if "FBI" in data[i]:
        answer += (str(i+1) + " ")

if answer == "":
    print("HE GOT AWAY!")
else:
    print(answer)
