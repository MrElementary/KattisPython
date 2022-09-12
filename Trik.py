x = input()

def A_move(z):
    return {1:2, 2:1, 3:3}[z]

def B_move(z):
    return {1:1, 2:3, 3:2}[z]

def C_move(z):
    return {1:3, 2:2, 3:1}[z]

start_pos = 1

for i in x:
    if i == "A":
        start_pos = A_move(start_pos)
    elif i == "B":
        start_pos = B_move(start_pos)
    else:
        start_pos = C_move(start_pos)

print(start_pos)
