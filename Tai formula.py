samples = int(input())

answer = 0

time = []
g_value = []

for i in range(samples):
    data = input().split()
    time.append(float(data[0]))
    g_value.append(float(data[1]))

for i in range(samples-1):
    answer += ((g_value[i] + g_value[i+1])/2) * (time[i+1] - time[i])

print(answer/1000)
