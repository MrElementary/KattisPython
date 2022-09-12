from collections import Counter

word = Counter(input())

guessing_list = list(input())

count = 0

for i in guessing_list:
    if len(word) == 0:
        break

    if i in word:
        del word[i]
    else:
        count += 1

if count < 10:
    print("WIN")
else:
    print("LOSE")
