comp_width, comp_height, stick_width, stick_height  = map(int,input().split())

if stick_width + 2 < comp_width:
    if stick_height + 2 < comp_height:
        print("1")
    else:
        print("0")
else: print("0")
