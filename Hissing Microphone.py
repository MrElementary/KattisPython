word = input()

counter = 0

for i in range(len(word)-1):
    if word[i] == "s":
        if word[i] == word[i+1]:
            counter += 1

if counter > 0:
    print("hiss")
else:
    print("no hiss")
