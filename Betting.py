def point():
    while True:
        try:
            first_percentage = input("Please enter the first percentage")
            x = float(first_percentage)
            if x <= 100 and x >= 0:
                y = 100/x
                z = 100/(100-x)
                print("{:.6f}".format(y))
                print("{:.6f}".format(z))
                break;
            if x > 100 or x < 0:
                print("Not a valid number")
        except ValueError:
            print("Not a valid number")
    
point()
