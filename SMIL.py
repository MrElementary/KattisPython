x = input()

for i in range(len(x)-1):
    if x[i] == ";" or x[i] == ":":
        if x[i+1] == "-":
            if x[i+2] == ")":
                print(i)
        elif x[i+1] == ")":
            print(i)
        else:
            continue
    else:
        continue
