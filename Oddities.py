test_cases = int(input())

for i in range(test_cases):
    value = int(input())
    if value % 2 != 0:
        print(value, "is odd")
    else:
        print(value, "is even")
