cord_1 = input().split()
cord_2 = input().split()
cord_3 = input().split()

cord_1x = cord_1[0]
cord_1y = cord_1[1]

cord_2x = cord_2[0]
cord_2y = cord_2[1]

cord_3x = cord_3[0]
cord_3y = cord_3[1]

def computation(x,y,z):
    if x == y:
        return z
    elif x == z:
        return y
    else:
        return x

missing_x = computation(cord_1x,cord_2x,cord_3x)
missing_y = computation(cord_1y,cord_2y,cord_3y)

print("{} {}".format(missing_x, missing_y))
    
