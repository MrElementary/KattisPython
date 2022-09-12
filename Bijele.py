x = list(map(int,input().split()))

y = [1,1,2,2,2,8]

answer = ""

for i in range(len(x)):
    value = y[i] - x[i]
    answer = answer + str(value) + " "

print(answer)
    
