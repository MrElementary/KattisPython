data = input()

new_data = []

multi_lis = [4,3,2,7,6,5,4,3,2,1]

count = 0

for char in data:
    if char != "-":
        new_data.append(int(char))


for i in range(0,10):
    count += new_data[i] * multi_lis[i]

if count % 11 == 0:
    print(1)
else:
    print(0)

