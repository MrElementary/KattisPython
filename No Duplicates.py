string = input().split()

my_dict = {}

for i in string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

if max(my_dict.values()) > 1:
    print("no")
else:
    print("yes")
