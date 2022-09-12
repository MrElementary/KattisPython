cases = int(input())


for i in range(cases):
    final = ""
    var_one = input()
    var_two = input()
    var_one = var_one.replace(" ","")
    var_two = var_two.replace(" ","")
    answer = int(var_one) + int(var_two)
    answer = str(answer)
    for i in answer:
        final += i + " "
    print(final[:-1])
