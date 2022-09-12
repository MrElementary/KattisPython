data = input().split()

card_type_string = ""

def split(word):
    global card_type_string
    for i in word:
        card_type_string += i[0]

split(data)

freq = {}

for i in card_type_string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
count = max(freq.values())

print(count)
