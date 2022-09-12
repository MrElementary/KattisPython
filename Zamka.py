lowervalue = int(input())
highervalue = int(input())
targetsum = int(input())

def calculation(value):
    value_text = str(value)
    total_value = 0
    for i in value_text:
        individual_value = int(i)
        total_value += individual_value
    return total_value


lowermatch = lowervalue
while calculation(lowermatch) != targetsum:
    lowermatch += 1

highermatch = highervalue
while calculation(highermatch) != targetsum:
    highermatch -= 1

print(lowermatch)
print(highermatch)
