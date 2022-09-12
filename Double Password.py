from itertools import product

data_one = input()
data_two = input()

comb = set(data_one + data_two)

perm = product(comb,repeat=4)

count = 0

for i in perm:
    if i[0] == data_one[0] or i[0] == data_two[0]:
        if i[1] == data_one[1] or i[1] == data_two[1]:
            if i[2] == data_one[2] or i[2] == data_two[2]:
                if i[3] == data_one[3] or i[3] == data_two[3]:
                    count += 1

print(count)
