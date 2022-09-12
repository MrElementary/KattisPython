cases = int(input())

for i in range(cases):
    data = list(map(int,input().split()))
    first_val = data[0]
    second_val = data[1]
    third_val = data[2]
    if first_val + second_val == third_val:
        print("Possible")
    elif first_val * second_val == third_val:
        print("Possible")
    elif abs(first_val - second_val) == third_val:
        print("Possible")
    elif first_val / second_val == third_val:
        print("Possible")
    elif second_val / first_val == third_val:
        print("Possible")
    else:
        print("Impossible")
