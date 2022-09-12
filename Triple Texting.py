message = input()

temp_list = []
first_word = ""
second_word = ""
third_word = ""

for i in message:
    temp_list.append(i)

value = len(temp_list)/3

for i in range(len(temp_list)):
    if i < value:
        first_word += temp_list[i]
    if i < (value*2) and i >= value:
        second_word += temp_list[i]
    if i >= (value*2):
        third_word += temp_list[i]
        
if first_word == second_word:
    print(first_word)
else:
    print(third_word)
