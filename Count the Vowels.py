x = input()

y = ["a","A","e","E","i","I","o","O","u","U"]

count = 0
def check(firstL, secondL):
    global count
    for i in firstL:
        if i in secondL:
            count = count + 1
    return count
check(x, y)
print(count)
    
