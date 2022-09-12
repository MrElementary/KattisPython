test_cases = int(input())

for i in range(test_cases):
    string_one = input()
    string_two = input()
    empty = ""
    for x,y in zip(string_one,string_two):
        if x == y:
            empty += "."
        else:
            empty += "*"
    print(string_one)
    print(string_two)
    print(empty)
    print("\n")
