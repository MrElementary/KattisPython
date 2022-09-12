
pos_one = 0
pos_two = 1
pos_three = 2


list_one = []
list_two = []
list_three = []

while pos_one < 300:
    list_one.append(pos_one)
    pos_one += 3

while pos_two < 300:
    list_two.append(pos_two)
    pos_two += 3

while pos_three < 300:
    list_three.append(pos_three)
    pos_three += 3


password = input().lower()

count = 0

new_pass = ""

for char in range(len(password)):
    if char in list_one:
        if password[char] != "p":
            count += 1
    if char in list_two:
        if password[char] != "e":
            count += 1
    if char in list_three:
        if password[char] != "r":
            count += 1

print(count)
            
        
