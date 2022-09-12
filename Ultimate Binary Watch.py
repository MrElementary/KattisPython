data = input()

temp_list = []

for char in data:
    temp_list.append(int(char))

first_output = []
second_output = []
third_output = []
fourth_output = []

for char in temp_list:
    if char <= 7:
        first_output.append(".")
    else:
        first_output.append("*")

    if char >=4 and char <= 7:
        second_output.append("*")
    else:
        second_output.append(".")

    if char in (2,3,6,7):
        third_output.append("*")
    else:
        third_output.append(".")

    if char in (1,3,5,7,9):
        fourth_output.append("*")
    else:
        fourth_output.append(".")


for x in first_output,second_output,third_output,fourth_output:
    x.insert(1," ")
    x.insert(3," ")
    x.insert(4," ")
    x.insert(5," ")
    x.insert(7," ")
    print(*x,sep='')

