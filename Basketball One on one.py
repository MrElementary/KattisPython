scoring = input()

score_a = 0
score_b = 0


for i in range(len(scoring)):
    if scoring[i] == "A":
        score_a += int(scoring[i+1])
    elif scoring[i] == "B":
        score_b += int(scoring[i+1])

if score_a > score_b:
    print("A")
else:
    print("B")
        
