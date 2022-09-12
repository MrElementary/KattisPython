questions = int(input())

answers = []


for i in range(questions):
    data = input()
    answers.append(data)

han_answers = answers[1:]

count = 0

for i in range(len(han_answers)):
    if han_answers[i] == answers[i]:
        count += 1

print(count)
        
