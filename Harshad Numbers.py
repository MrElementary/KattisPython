number = int(input())

numberstr = str(number)

total = 0

for i in numberstr:
    i = int(i)
    total += i

def sum_val():
    global numberstr
    global number
    global total
    if number % total == 0:
        print(number)
    else:
        number += 1
        numberstr = str(number)
        total = 0
        for i in numberstr:
            i = int(i)
            total += i
        sum_val()

sum_val()
