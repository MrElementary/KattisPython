from operator import itemgetter

cups = int(input())

final_list = []

for i in range(cups):
    x = input().split()
    if x[0].isdigit():
        x[0] = int(x[0]) / 2
        final_list.append([x[1],x[0]])
    else:
        final_list.append([x[0],int(x[1])])

x = sorted(final_list,key=itemgetter(1))

for i in x:
    print(i[0])
