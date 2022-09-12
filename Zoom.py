list_r, skip_val = map(int,input().split())
temp_list = list(map(int,input().split()))

for i in range(skip_val-1,list_r,skip_val):
    print(temp_list[i])
