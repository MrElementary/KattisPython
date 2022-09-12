names = input().split()

first_name = names[0]
second_name = names[1]

vowels = ["a","i","o","u"]

new_name = ""

if first_name[-1] == "e":
    new_name = first_name+"x"+second_name
elif first_name[-1] in vowels:
    first_name = first_name[0:-1]
    new_name = first_name+"ex"+second_name
elif first_name[-1] == "x":
    if first_name[-2] == "e":
        new_name = first_name+second_name
else:
    new_name = first_name+"ex"+second_name

print(new_name)
