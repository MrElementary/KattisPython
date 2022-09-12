x = input()
y = int(x)
def subtract():
    global y
    while y >= 2:
        y = y -2
    return y
subtract()
if y == 1:
    print("Alice")
if y == 0:
    print("Bob")
