data = int(input())

count = 7

for i in range(data):
    text = input()
    if text == "Skru op!":
        if count < 10:
            count += 1
        else:
            count == 10
    if text == "Skru ned!":
        if count > 0:
            count -= 1
        else:
            count == 0

print(count)
        
