data = input()

half_calc = int(len(data)/2)

first_half = data[0:half_calc]
second_half = data[half_calc:]

def letter_conversion(letters):
    value = ord(letters) - 65
    return value

def rotate(half_encrypt):
    count = 0
    new_half = ""
    for i in half_encrypt:
        count += letter_conversion(i)
    while count > 26:
        count -= 26
    for i in half_encrypt:
        temp_val_one = letter_conversion(i) + count
        if temp_val_one >= 26:
            temp_val_one = temp_val_one - 26
        temp_val_two = temp_val_one + 65
        new_half += chr(temp_val_two)
    return new_half

first_half_done = rotate(first_half)
second_half_done = rotate(second_half)

def merge():
    string_value = ""
    for i in range(len(second_half_done)):
        value = letter_conversion(first_half_done[i]) + letter_conversion(second_half_done[i])
        if value >= 26:
            value = value - 26
        temp_val = value + 65
        string_value += chr(temp_val)
    return(string_value)
           
print(merge())
        
    
    
    
