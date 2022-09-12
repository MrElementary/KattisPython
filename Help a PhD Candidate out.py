cases = int(input())

for i in range(cases):
    data = input().split("+")
    if data[0] == "P=NP":
        print("skipped")
    else:
        val_one = int(data[0])
        val_two = int(data[1])
        print(val_one+val_two)
