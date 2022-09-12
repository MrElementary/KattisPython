x = input()

walls = x.index("()")
if len(x[0:walls]) == len(x[walls+1:-1]):
                         print("correct")
else:
    print("fix")
