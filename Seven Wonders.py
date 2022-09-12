x = input()
data = list()

total_t = 0
total_c = 0
total_g = 0

for i in range(len(x)):
    data.append(x[i])

for value in data:
    if value == "T":
        total_t += 1
    if value == "C":
        total_c += 1
    if value == "G":
        total_g += 1

numberofsets = min(total_t, total_c, total_g)

total_cards = pow(total_t,2) + pow(total_c,2) + pow(total_g,2) + numberofsets*7

print(total_cards)

