line_len = int(input())

pos = list(map(int,input().split()))

temp_list = [None]*line_len

temp_list[0] = 1

for i in range(len(pos)):
    temp_list[1+pos[i]] = 2+i

temp_string = " ".join(str(item) for item in temp_list)

print(temp_string)

