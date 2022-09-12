data = input().split()

left = int(data[0])
right = int(data[1])

most = max(left,right)

if (left+right) == 0:
    print("Not a moose")
else:
    if (left+right)%2 == 0:
        if left == right:
            print("Even",most*2)
        else:
            print("Odd",most*2)
    else:
        print("Odd",most*2)
